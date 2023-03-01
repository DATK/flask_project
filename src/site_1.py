import json


# File for registration

class Reg_or_chek_reg:
    """ADD  reg and reg if not reg"""

    def __init__(self, data="data.txt"):
        self.data = data
        # with open(self.data, "w", encoding="UTF-8") as f:
        #    f.write("{}")

    def chek_reg(self, key):
        with open(self.data, "r", encoding="UTF-8") as f:
            if f.readline != "{}":
                regs = json.load(f)
            else:
                return ("data is clear")
        if key in regs:
            return True
        else:
            return False

    def reg(self, key, val):
        with open(self.data, "r", encoding="UTF-8") as f:
            vr = json.load(f)
        vr[key] = val
        with open(self.data, "w", encoding="UTF-8") as f:
            vr = json.dump(vr, f)

    def clear_data(self):
        with open(self.data, "w", encoding="UTF-8") as f:
            f.write("{}")

    def vhode(self, key, val):
        with open(self.data, "r", encoding="UTF-8") as f:
            if f.readline != "{}":
                regs = json.load(f)
        try:
            if regs[key] == val:
                return True
            else:
                return False
        except KeyError:
            return False


def read_html(file):
    file = "./html/" + file
    with open(file, "r", encoding="UTF-8") as f:
        html = f.read()
    return html
