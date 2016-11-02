import random

"""
IMEI validation (CRC check) and fake IMEI generation.

You can find more documentation about IMEI here:

http://en.wikipedia.org/wiki/International_Mobile_Station_Equipment_Identity
"""

class ImeiSupport:
    """
    Class for IMEI validation and fake IMEIs generation (by known IMEI). Can check that 15-digit IMEI (std.
    length of IMEI) is valid. Or can generate needful amount of fake IMEI by any known IMEI.
    """

    IMEI_LENGTH = 15

    @staticmethod
    def next(imei):
        """
        Generates next IMEI for the given IMEI. So, using this method you can can generate needful amount of fake IMEIs
        (for example, for testing purpose).

        :param imei: string or integer representation of 15-digit IMEI (std. length of IMEI)

        :return: next value for IMEI
        """
        imei = int(imei)

        imei += 10

        imei //= 10
        check = ImeiSupport.checksum(imei)

        return imei * 10 + check

    @staticmethod
    def checksum(imei):
        """
        Generates check sum for IMEI

        :param imei: string or integer representation of 15-digit IMEI or 14-digits IMEI without CRC.

        :return: checksum for IMEI. If you entered 15-digit (std. IMEI) and IMEI is correct it's will be the same as last
        15-th digit
        """
        imei = int(imei)

        if len(str(imei)) == ImeiSupport.IMEI_LENGTH:
            imei //= 10

        sum = [0] * (ImeiSupport.IMEI_LENGTH-1)

        mod = 10
        for i in range(1, ImeiSupport.IMEI_LENGTH):
            index = i - 1
            sum[index] = int(imei % mod)

            if i % 2 != 0:
                sum[index] *= 2

            if sum[index] >= 10:
                sum[index] = int(sum[index] % 10 + (sum[index] / 10))

            imei /= mod

        check = 0

        for i in range(len(sum)):
            check += sum[i]

        return (check * 9) % 10

    @staticmethod
    def isValid(imei):
        """
        Check that IMEI is valid.

        :param imei: string or integer representation of 15-digit IMEI (std. IMEI)

        :return: True when IMEI is correct, False otherwise
        """

        imei = int(imei)
        crc = ImeiSupport.checksum(imei // 10)

        return crc == (imei % 10)

    @staticmethod
    def generateNew():
        """
        Generates random IMEI number

        :return: fake IMEI number
        """
        imei = 0

        qty = ImeiSupport.IMEI_LENGTH
        while qty > 0:

            if qty != ImeiSupport.IMEI_LENGTH:
                imei = imei * 10 + random.randint(0, 9)
            else:
                imei = random.randint(1, 9)

            qty -= 1

        crc = ImeiSupport.checksum(imei)

        imei = imei * 10 + crc

        assert ImeiSupport.isValid(imei) == True
        assert ImeiSupport.isValid(str(imei)) == True

        return str(imei)

    @staticmethod
    def test():
        """
        Makes tests for this class

        :return: True if everything is OK
        """

        check = ImeiSupport.checksum(35806501910426)
        assert check == 5

        check = ImeiSupport.checksum("35806501910426")
        assert check == 5

        check = ImeiSupport.checksum(358065019104265)
        assert check == 5

        check = ImeiSupport.checksum("358065019104265")
        assert check == 5

        check = ImeiSupport.checksum(35780502398494)
        assert check == 2

        check = ImeiSupport.checksum(35693803564380)
        assert check == 9

        check = ImeiSupport.checksum(49015420323751)
        assert check == 8

        check = ImeiSupport.checksum(490154203237518)
        assert check == 8

        check = ImeiSupport.checksum("49015420323751")
        assert check == 8

        assert ImeiSupport.isValid(358065019104265) == True
        assert ImeiSupport.isValid(357805023984942) == True
        assert ImeiSupport.isValid(356938035643809) == True

        assert ImeiSupport.isValid(358065019104263) == False
        assert ImeiSupport.isValid(357805023984941) == False
        assert ImeiSupport.isValid(356938035643801) == False

        assert ImeiSupport.next(358065019104273) == 358065019104281

        assert ImeiSupport.next(357805023984942) == 357805023984959
        assert ImeiSupport.next(356938035643809) == 356938035643817

        return True

if __name__ == '__main__':
    ImeiSupport.test()
    print("TEST SUCCESSFULLY FINISHED")

