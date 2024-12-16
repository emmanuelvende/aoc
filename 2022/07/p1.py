import re
import sys

class FileSystemManager:
    def __init__(self):
        self.filesystem_tmp = []
        self.curdirname = []
        self.filesystem_final = []

    def parse_for_command(self, s):
        s = s[:-1]  # remove \n
        m = re.match(r"^\$", s)
        if m:
            if s == "$ ls":
                print("listing")
            elif s == "$ cd ..":
                self.up()
            else:
                n = re.match(r"\$ cd (?P<dirname>[\w\/]+)", s)
                dirname = n.group("dirname")
                print(f"!!! FOUND {dirname=}")
                self.cd_in(dirname)
        return bool(m)

    def parse_for_file_info(self, s):
        m = re.search(r"^(?P<filesize>\d+) (?P<filename>[\w\.]+)", s)
        if m:
            filesize = int(m.group("filesize"))
            filename = m.group("filename")
            self.add_file(filename, filesize)
        return bool(m)

    def parse_for_dir_info(self, s):
        m = re.search(r"^dir (?P<dirname>\w+)", s)
        if m:
            dirname = m.group("dirname")
            self.add_dir(dirname)
        return bool(m)

    def cd_in(self, dirname):
        print(f"cd_in {dirname}")
        self.curdirname.append(dirname)
        self.filesystem_tmp.append(["/".join(self.curdirname), [], []])

    def up(self):
        print("up", end="  ")
        self.curdirname.pop()
        self.filesystem_final.append(self.filesystem_tmp.pop())

    def add_file(self, filename, filesize):
        print(f"add_file : {filename}, {filesize}", end="  ")
        self.filesystem_tmp[-1][2].append((filename, filesize))

    def add_dir(self, dirname):
        print(f"add_dir {dirname}", end="  ")
        self.filesystem_tmp[-1][1].append(dirname)

    def finalize(self):
        while len(self.filesystem_tmp) > 0:
            self.up()
        # self.fs_final.reverse()

    def compute_directories_sizes(self):
        self.dirs_sizes_dict = {}
        for directory in self.filesystem_final:
            directory_name = directory[0]
            files = directory[2]
            total_size = 0
            for f in files:
                filename, filesize = f
                total_size += filesize
            self.dirs_sizes_dict[directory_name] = total_size
            sub_directories = directory[1]
            for sub_directory in sub_directories:
                self.dirs_sizes_dict[directory_name] += self.dirs_sizes_dict[
                    "/".join((directory_name, sub_directory))
                ]


with open(sys.argv[1], "r") as f:
    lines = f.readlines()


filesystem_manager = FileSystemManager()


def fail(a):
    assert 0


for line in lines:
    print(f"*** {line[:-1]} ***", end=" --> ")
    for action, action_name in (
        (filesystem_manager.parse_for_command, "parse_for_command"),
        (filesystem_manager.parse_for_dir_info, "parse_for_dir_info"),
        (filesystem_manager.parse_for_file_info, "parse_for_file_info"),
        (fail, ""),
    ):
        print(f"{action_name}", end=" --> ")
        success = action(line)
        if success:
            print("DONE")
            break
        print("NEXT")

print("FINALIZE...")
filesystem_manager.finalize()

print(filesystem_manager.filesystem_tmp)

print("!!! FINAL !!!")
for x in filesystem_manager.filesystem_final:
    print(x)

print(f"{len(filesystem_manager.filesystem_final)} directories")

filesystem_manager.compute_directories_sizes()

for x in filesystem_manager.dirs_sizes_dict.items():
    print(x)

total_size_of_dirs_of_at_most_100000 = 0
for x in filesystem_manager.dirs_sizes_dict.values():
    if x <= 100000:
        total_size_of_dirs_of_at_most_100000 += x
print(f"{total_size_of_dirs_of_at_most_100000=}")
