def copy_file(filename1, filename2):
    orig = open(filename1, "r")
    dest = open(filename2, "w")
    for line in orig:
        dest.write(line)
    orig.close()
    dest.close()


copy_file("C:\Isaac\Desktop\PyProgram\ExercisesTy\script.txt", "C:\Isaac\Desktop\PyProgram\ExercisesTy\secfile.txt")