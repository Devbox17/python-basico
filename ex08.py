d1 = float(input('Digite uma distância em metros: '))
km = d1 / 1000
hm = d1 / 100
dam = d1 / 10
dm = d1 * 10
cm = d1 * 100
mm = d1 * 1000

print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))