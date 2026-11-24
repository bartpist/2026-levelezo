import platform
import random

def bi_generate_id(start=1000, end=9999):
    return random.randint(start, end)

class BiSystemInfo:
    def __init__(self):
        self.os_name = ""
        self.os_release = ""
        self.host_name = ""
        self.architecture = ""
        self.processor = ""
        self.check_id = 0

    def refresh(self):
        self.os_name = platform.system()
        self.os_release = platform.release()
        self.host_name = platform.node()
        self.architecture = platform.machine()
        self.processor = platform.processor()
        self.check_id = bi_generate_id()

    def top_banner(self):
        return f"Host: {self.host_name} | OS: {self.os_name} {self.os_release} | ID: #{self.check_id}"

    def detail_lines(self):
        return [
            f"Operating System: {self.os_name} {self.os_release}",
            f"Host Name: {self.host_name}",
            f"Architecture: {self.architecture}",
            f"Processor: {self.processor}",
            f"Check ID: {self.check_id}",
        ]

    def save_to_file(self, filename ="system_report.txt"):
        with open(filename, "w", encoding="utf-8") as file:
            file.write("BI_System_Checker_Report\n")
            file.write("-" * 30 + "\n")
            for line in self.detail_lines():
                file.write(line + "\n")