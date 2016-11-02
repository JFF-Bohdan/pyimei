from pyimei import ImeiSupport

def checkImeisArray(imeis):
    for imei in imeis:
        if ImeiSupport.isValid(imei):
            print("IMEI: '{}' is valid".format(imei))
        else:
            print("IMEI '{}' is NOT valid".format(imei))

#testing classes
ImeiSupport.test()

valid_imeis = [
    356938035643809,
    490154203237518,
    "356938035643809"
]

invalid_imeis = [
    358065019104263,
    "357805023984941",
    356938035643801
]

checkImeisArray(valid_imeis)
checkImeisArray(invalid_imeis)

print("Generating independent FAKE imeis...")
RANDOM_IMEIS_QTY = 5
for i in range(RANDOM_IMEIS_QTY):
    print("\tfake IMEI[{}] = {}".format(i+1, ImeiSupport.generateNew()))

print("Generating sequental FAKE imeis:")
DEP_RANDOM_IMEIS_QTY = 5

startImei   = ImeiSupport.generateNew()
currentImei = startImei
print("start IMEI: {}".format(startImei))

for i in range(RANDOM_IMEIS_QTY):
    currentImei = ImeiSupport.next(currentImei)
    print("\tfake IMEI[{}] = {}".format(i+1, currentImei))



print("DONE")