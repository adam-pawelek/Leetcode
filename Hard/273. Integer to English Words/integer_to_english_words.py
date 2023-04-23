class Solution:

    def __init__(self):
        self.num_dict = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        bilion = False
        milion = False
        thousand = False
        result_word = ""
        was_num = False

        while num > 0:
            print(num)

            help_num = num
            if help_num // (10 ** 9):
                bilion = True
                help_num = help_num // (10 ** 9)
            elif bilion and was_num:
                result_word += " Billion"
                bilion = False
                was_num = False

            if help_num // (10 ** 6):
                milion = True
                help_num = help_num // (10 ** 6)
            elif milion and num < 10 ** 6 and was_num:
                result_word += " Million"
                milion = False
                was_num = False

            if help_num // (10 ** 3):
                thousand = "True"
                help_num = help_num // (10 ** 3)
            elif thousand and num < 10 ** 3 and was_num:
                result_word += " Thousand"
                thousand = False
                was_num = False

            if result_word != "":
                result_word += " "
            if help_num >= 100:
                result_word += self.num_dict[help_num // 100]
                result_word += " Hundred"
                was_num = True
            elif help_num >= 20:
                result_word += self.num_dict[(help_num // 10) * 10]
                was_num = True
            elif help_num >= 10 and help_num < 20:
                result_word += self.num_dict[help_num]
                num = str(num)
                num = num[1:]
                was_num = True
            elif help_num > 0:
                result_word += self.num_dict[help_num]
                was_num = True

            num = str(num)
            if len(num) > 1:
                num = num[1:]
                num = int(num)
            else:
                num = 0

        if bilion:
            result_word += " Billion"
            bilion = False

        if milion and num < 10 ** 6:
            result_word += " Million"
            milion = False

        if thousand and num < 10 ** 3:
            result_word += " Thousand"
            thousand = False

        return result_word







