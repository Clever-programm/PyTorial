import traceback


class Results:
    def __init__(self, *inputs):
        self.prints = list()
        self.inputs = [[j for j in i] for i in inputs]

    def add_print(self, *texts):
        self.prints.append(' '.join(map(str, texts)) + '\n')

    def get_prints(self):
        return self.prints

    def my_input(self, *texts):
        self.prints.append(' '.join(map(str, texts)))
        if self.inputs:
            a = self.inputs[0][0]
            self.inputs[0].pop(0)
            return a
        return None


def check(texts, *inputs):
    res = Results(inputs)
    input = res.my_input
    print = res.add_print
    try:
        exec(texts)
        return res.get_prints()
    except Exception:
        return str(traceback.format_exc())


