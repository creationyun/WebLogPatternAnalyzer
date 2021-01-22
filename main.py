import re
import os

INPUT_DIR = 'Server2'
lineformat = re.compile(r"""(?P<ipaddress>IP\d{7}) (.+ ){2,3}\[(?P<dateandtime>\d{2}\/[A-Za-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST|OPTIONS|HEAD|PUT|DELETE|CONNECT|TRACE|PATCH)) (?P<url>.*)(?P<protocol>.+)\s*\") (?P<statuscode>\-|\d{3}) (?P<bytessent>\-|\d+)""", re.IGNORECASE)

parsed = 0
lines = 0

if __name__ == "__main__":
    for f in os.listdir(INPUT_DIR):
        logfile = open(os.path.join(INPUT_DIR, f))

        for ln in logfile.readlines():
            lines += 1

            data = re.search(lineformat, ln)
            if data:
                parsed += 1
                datadict = data.groupdict()
                # print(datadict)
            else:
                print(ln)

        logfile.close()
