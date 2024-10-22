from extract_from_dat import extract_from_dat

def main():
    input_file = './data.dat'  
    output_file = 'data.csv'
    sample_mass, sample_molecular_weight, df = extract_from_dat(input_file, output_file)
    print(f'Sample Mass: {sample_mass}')
    print(f'Sample Molecular Weight: {sample_molecular_weight}')


if __name__ == '__main__':
    main()
