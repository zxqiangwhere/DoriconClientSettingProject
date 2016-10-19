

class mmc:
    def method(self):
        message = None
        if 1 > 2:
            message = "ok"
        if 1 > 3:
            message = "error"
        return message
    def getvalue(self):
        mm = self.method()
        print(mm)




if __name__ == '__main__':
    m = mmc()
    m.getvalue()
# mm = method()
# print(mm)
