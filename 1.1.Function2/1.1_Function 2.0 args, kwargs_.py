def adv_print(*args, start='\n', max_line=int(), in_file=False):
    if max_line:
        p_list = list()
        m = max_line
        for a in args:
            p_list.append(a)
        p_list = start + ' '.join([str(a) for a in p_list])
        counter = 0

        for a in range(int(len(p_list) / m) + 1):
            if in_file:
                with open('file.txt', 'a', encoding='utf-8') as f:
                    f.write(p_list[counter:max_line] + '\n')
                    counter += m
                    max_line += m
            else:
                print(p_list[counter:max_line])
                counter += m
                max_line += m

    else:
        print(start, *args)


adv_print('Арозаупалана лапуАзора', 467392765, max_line=7, in_file=True)
