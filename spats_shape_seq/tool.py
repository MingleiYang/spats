
import ConfigParser
import datetime
import os
import subprocess
import sys
import time


class SpatsTool(object):

    def __init__(self, path):
        self.no_config_required_commands = [ "viz" ]
        self.path = path or os.getcwd()
        self.config = None
        self.cotrans = False
        self.skip_log = False
        self._parse_config()

    def _parse_config(self):
        config_path = os.path.join(self.path, "spats.config")
        if not os.path.exists(config_path):
            return
        parser = ConfigParser.SafeConfigParser()
        parser.read(config_path)
        config = {}
        for section in parser.sections():
            if section not in config:
                config[section] = {}
            for name, value in parser.items(section):
                config[section][name] = value
        if config and 'spats' in config:
            self.config = config['spats']
            if 'cotrans' in self.config:
                cotrans = self.config['cotrans']
                self.cotrans = False if (cotrans == 'False') else bool(cotrans)

    def _native_tool(self, tool_name):
        import spats_shape_seq
        bin_path = os.path.join(os.path.dirname(spats_shape_seq.__file__), "../native/bin", tool_name)
        return bin_path if os.path.exists(bin_path) else None

    def _add_note(self, note):
        self._notes.append(note)
        print(":{}".format(note))

    def run(self, command):

        if not self.config and command not in self.no_config_required_commands:
            print("Missing spats.config")
            return

        self._notes = []
        start = time.time()
        hdlr = getattr(self, command, None)
        if not hdlr:
            print("Invalid command: {}".format(command))
            return
        hdlr()
        delta = time.time() - start
        if not self.skip_log:
            self._log(command, delta)

    def _log(self, command, delta):
        stamp = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')
        with open(os.path.join(self.path, 'spats.log'), 'ab') as outfile:
            outfile.write("{} : {}, {}s\n".format(stamp, command, int(delta)))
            for note in self._notes:
                outfile.write("   - {}\n".format(note))
            outfile.write("\n")
                
    def reads(self):

        from spats_shape_seq.reads import ReadsData, ReadsAnalyzer

        db_basename = 'reads.spats'
        db_name = os.path.join(self.path, db_basename)
        if os.path.exists(db_name):
            self._add_note("** removing previous {}".format(db_basename))
            os.remove(db_name)

        native_tool = self._native_tool('reads')
        if native_tool:
            self._add_note("using native reads")
            subprocess.check_call([native_tool, self.config['target'], self.config['r1'], self.config['r2'], db_name], cwd = self.path)

        data = ReadsData('reads.spats')
        if not native_tool:
            self._add_note("using python reads")
            data.parse(self.config['target'], self.config['r1'], self.config['r2'])

        analyzer = ReadsAnalyzer(data, cotrans = self.cotrans)
        analyzer.process_tags()
        self._add_note("tags processed to {}".format(db_basename))

    def process(self):

        run_basename = 'run.spats'
        run_name = os.path.join(self.path, run_basename)
        if os.path.exists(run_name):
            self._add_note("** removing previous {}".format(run_basename))
            os.remove(run_name)

        native_tool = self._native_tool('cotrans')
        if self.cotrans and native_tool:
            self._add_note("using native cotrans processor")
            subprocess.check_call([native_tool, self.config['target'], self.config['r1'], self.config['r2'], run_name], cwd = self.path)

        else:
            self._add_note("using python cotrans processor")
            from spats_shape_seq import Spats
            spats = Spats(cotrans = self.cotrans)
            spats.addTargets(self.config['target'])
            spats.process_pair_data(self.config['r1'], self.config['r2'])
            spats.store(run_name)

    def validate(self):
        run_basename = 'run.spats'
        run_name = os.path.join(self.path, run_basename)
        if not os.path.exists(run_name):
            print("Missing: {}".format(run_basename))
            return
        from spats_shape_seq import Spats
        spats = Spats()
        spats.load(run_name)
        if spats.validate_results(self.config['r1'], self.config['r2']):
            self._add_note("Validation pass")
        else:
            self._add_note("Validation FAILURE")

    def viz(self):
        self.skip_log = True
        if sys.platform != "darwin":
            print("Invalid platform for viz UI: {}".format(sys.platform))
            return
        import spats_shape_seq
        base_path = os.path.join(os.path.dirname(spats_shape_seq.__file__), "..")
        subprocess.check_call(["make", "viz"], cwd = base_path)
        
        
        

def run(command, path = None):
    SpatsTool(path).run(command)


if __name__ == '__main__':
    run(sys.argv[1])
