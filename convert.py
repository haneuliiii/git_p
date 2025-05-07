
def convert(p3file,p6file):
    with open(p6file, 'rb') as f:
        magic_num = f.readline().strip()
        if magic_num != b'P6':
            raise ValueError('Not a valid P6 PPM file')

        def read_non_comment_line():
            line = f.readline()
            while line.startswith(b'#'):
                line = f.readline()
            return line

        size_line = read_non_comment_line()
        width, height = map(int, size_line.strip().split())
        maxval = int(read_non_comment_line().strip())

        pixel_data = f.read(width * height * 3)

        with open(p3file, 'w') as out:
            out.write('P3\n')
            out.write(f'{width} {height}\n')
            out.write(f'{maxval}\n')

            for i in range(0, len(pixel_data), 3):
                r, g, b = pixel_data[i], pixel_data[i+1], pixel_data[i+2]
                out.write(f'{r} {g} {b}\n')



convert("converted_32217216.txt","/home/data/colorP6File.ppm")
