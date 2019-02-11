from decorator import logging

if __name__ == '__main__':
    @logging('logging.txt')
    def adv_print(*args, start='\n', max_line=int(), in_file=False):
        p_list = list()
        m = max_line
        for a in args:
            p_list.append(a)
        p_list = start + ' '.join([str(a) for a in p_list])
        counter = 0

        for a in range(int(len(p_list) / m) + 1):
            if in_file:
                with open(in_file, 'a', encoding='utf-8') as f:
                    print(p_list[counter:max_line])
                    f.write(p_list[counter:max_line] + '\n')
                    counter += m
                    max_line += m
            else:
                print(p_list[counter:max_line])
                counter += m
                max_line += m


    adv_print('Арозаупалана лапуАзора', 467392765, max_line=7, in_file='file.txt')
