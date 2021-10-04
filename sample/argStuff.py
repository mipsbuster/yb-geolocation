print('args')
totalRecords = 1
run_option = ''

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
print('Length of args ', len(sys.argv))

if len(sys.argv) != 2:
    print("Usage: ./workloads.py  -h -m <total_records_to_insert> -s <inster_one>")
    print("Note: enter a note here ','")
    exit(1)
opts, arg = getopt.getopt(sys.argv[1:], "hi:o:si-0", "m=:0")
for k, v in opts:
    try:
        if k == '-h':
            print("command is help")
            print("Usage: ./workloads.py  -h -m <total_records_to_insert> -s <insert_one>")
            print("Note: enter a note here ','")
        if k == '-m':
            print('command is many')
        if k == '-s':
            print('command is single')
    except:
        print("error")
        print('workloads.py -m <qty> -s ')