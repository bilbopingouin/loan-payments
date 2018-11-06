
notar_commission = 3.5
taxes = 1.5

data = {'current debt': 0, 'current year': 0}

def get_value(name):
    vfloat = 0.0
    while True:
        print'Please enter the '+name+':',
        v_raw = input()
        try:
            vfloat = float(v_raw)
        except:
            print('Format not understood')
        else:
            if vfloat >= 0:
                break
            else:
                print('Numbers should be positive')
    return vfloat
 

def get_inputs():
    list_values = ['interest rate','monthly paiement','fixed years','yearly extra transfer']

    print('Enter debt [1] or calculate debt [2]? Please enter 1 or 2: ')
    v=get_value('choice')
    while v!=1.0 and v!=2.0:
        print('You entered:',v)
        v=get_value('choice (1 or 2)')
    if v == 1.0:
        list_values.insert(0,'original debt')
    else:
        price = get_value('price')
        capital = get_value('capital')
        commission = get_value('commission (3.57)')
        data['original debt'] = price*((100.0+commission+notar_commission+taxes)/100.0) - capital

    for value in list_values:
        data[value] = get_value(value)
    
    data['current debt'] = data['original debt']
    
def print_data():
    print('\n---\nCurrent status:')
    for name,value in data.items():
        print(' {:<24s}: {:>10.2f}'.format(name,value))

def calculate_yearly():
    data['current year'] += 1
    interests = data['current debt']*data['interest rate']/100.0
    total_paid = data['monthly paiement']*12
    if total_paid+data['yearly extra transfer']<data['current debt']:
        tilgung = total_paid - interests
        data['current debt'] -= (tilgung+data['yearly extra transfer'])
        extra = data['yearly extra transfer']
    elif data['current debt'] == 0:
        interests = 0
        tilgung   = 0
        extra     = 0
    else:
        if total_paid<data['current debt']:
            extra = data['current debt'] - total_paid
        else:
            total_paid = data['current debt']
            extra = 0
        tilgung = total_paid - interests
        data['current debt'] = 0
    return (interests,tilgung,extra)
    
def calculate_fixed_years():
    output_line = '{:>6s} | {:>15s} {:>15s} {:>15s} | {:>15s} | {:>15s}'
    data_output_line = '{:>6d} | {:>15.2f} {:>15.2f} {:>15.2f} | {:>15.2f} | {:>15.2f}'
    print('\n---')
    print(output_line.format('Year','Pay/month','Reimb/month','Inter/month','Irreg reimb','Rest debt'))
    print('-'*len(output_line.format(' ',' ',' ',' ',' ',' ')))
    for y in range(int(data['fixed years'])):
        i,t,e = calculate_yearly()
        print(data_output_line.format(data['current year'],(t+i)/12.0,t/12.0,i/12.0,e,data['current debt']))

if __name__ == '__main__':
    get_inputs()

    print_data()

    calculate_fixed_years()

    print_data()

    print('\nPress enter...')
    try:
        input()
    except:
        pass
