import os
import sys
import stat
import time
import shutil


class historyManager(object):
    def __init__(self):
        self.command_history = []


    def push_command(self,cmd):
        self.command_history.append(cmd)
        
 
    def get_commands(self):
        return self.command_history
        

    def number_commands(self):
        return len(self.command_history)


class parserManager(object):
    def __init__(self):
        self.parts = []

    def parse(self,cmd):
        self.parts = cmd.split(" ")
        return self.parts
        

class commandManager(parserManager):
    def __init__(self):
        self.command = None


    def run_command(self,cmd):
        self.command = cmd
        self.command = self.parse(self.command)
        return self.command


    def ls(self):
        for file in os.listdir('.'):
            if os.path.isfile(file):
                print(file)
            else:
                print(file,"/")
    def lsf(self,flag):
        files_info=[]
        for file_name in os.listdir('.'):
            file_stats=os.stat(file_name)
            file_info = [
            file_name,
            file_stats [stat.ST_SIZE],
            oct(stat.S_IMODE(file_stats.st_mode))[2:],
            time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_MTIME])),
            time.strftime("%m/%d/%Y %I:%M:%S %P",time.localtime(file_stats[stat.ST_ATIME])),
            time.strftime("%m/%d/%Y &I:%M:%S %p",time.localtime(file_stats[stat.ST_CTIME]))
            ]
            files_info.append(file_info)
        if(flag=='-l'):
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("File Name","Size","Mode","Mtime","Atime","Ctime"))
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("---------","----","----","-----","-----","-----"))
            for file in files_info:
                print('{}\t\t{}\t{}\t{}\t{}\t{}'.format(file[0],file[1],file[2],file[3],file[4],file[5]))
        elif(flag=='-s'):
            files_info.sort(key=lambda x:int(x[1]))
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("File Name","Size","Mode","Mtime","Atime","Ctime"))
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("---------","----","----","-----","-----","-----"))
            for file in files_info:
                print('{}\t\t{}\t{}\t{}\t{}\t{}'.format(file[0],file[1],file[2],file[3],file[4],file[5]))
        elif(flag=='-m'):
            files_info.sort(key=lambda x:time.strftime(x[3]))
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("File Name","Size","Mode","Mtime","Atime","Ctime"))
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("---------","----","----","-----","-----","-----"))
            for file in files_info:
                print('{}\t\t{}\t{}\t{}\t{}\t{}'.format(file[0],file[1],file[2],file[3],file[4],file[5]))
        elif(flag=='-a'):
            files_info.sort(key=lambda x:time.strftime(x[4]))
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("File Name","Size","Mode","Mtime","Atime","Ctime"))
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("---------","----","----","-----","-----","-----"))
            for file in files_info:
                print('{}\t\t{}\t{}\t{}\t{}\t{}'.format(file[0],file[1],file[2],file[3],file[4],file[5]))
        elif(flag=='-c'):
            files_info.sort(key=lambda x:time.strftime(x[5]))
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("File Name","Size","Mode","Mtime","Atime","Ctime"))
            print('{}\t{}\t{}\t\t{}\t\t\t{}\t\t\t{}'.format("---------","----","----","-----","-----","-----"))
            for file in files_info:
                print('{}\t\t{}\t{}\t{}\t{}\t{}'.format(file[0],file[1],file[2],file[3],file[4],file[5]))
        else:
            print("flag is un recognised")
    def cp(self,source,destination):
        if(os.path.isfile(source)):
            shutil.copy(source,destination)
            print("file copied succesfully")
        else:
            print("file does not exist")
    def chmod(self,file):
        if(os.path.isfile(file)):
            os.chmod(file,0o777)
            print("mode changed succesfully")
        else:
            print("file does not exist")
        
    def cd(self,directory):
        if directory=='..':
            os.chdir('..')
            new=os.getcwd()
            print(new)
        elif directory=='~':
            home=os.path.expanduser('~')
            os.chdir(home)
            new=os.getcwd()
            print(new)
        else:
            if os.path.isdir(directory):
                os.chdir(directory)
                new=os.getcwd()
                print(new)
            else:
                print("directory  does not exist")
    def wc(self,flag,file):
        if(os.path.isfile(file)):
            num_lines = 0
            num_words = 0
            num_chars = 0
            with open(file, 'r') as f:
                for line in f:
                    words = line.split()
                    num_lines += 1
                    num_words += len(words)
                    num_chars += len(line)
            if flag=="0":
                print(num_lines)
                print(num_words)
                print(num_chars)
            elif(flag=="-l"):
                print(num_lines)
            else:
                print("flag does not exist")
        else:
            print("file does not exist")
    def history(self):
        his=historyManager.get_commands(self)
        return his
        
    def rm(self,file):
        if(os.path.isfile(file)):
            os.remove(file)
            print("file removed succesfully")
        else:
            print("file does not exist")
    def mv(self,source,destination):
        if(os.path.isfile(source)):
            shutil.move(source,destination)
            print("file renamed succesfully")
        else:
            print("file does not exist")
            

   
    def cat(self,file):
        if(os.path.isfile(file)):
            f = open(file,'r')
            print(f.read())
        else:
            print("file does not exist")
        

class driver(object):
    def __init__(self):
        self.history = historyManager()
        self.commands = commandManager()
        self.number_commands = 0
        
 
    def runShell(self):
        number_commands = 0
        while True:
            self.input = input("input-$" )         # get command
            self.history.push_command(self.input)   # put in history
            parts = self.commands.run_command(self.input)
            #print(int(111,8))
            if parts[0]=='cat':
                if len(parts)==2:
                    self.commands.cat(parts[1])
                else:
                    print("file arguments  missing for cat command")
            elif parts[0]=='ls':
                if(len(parts)==1):
                    self.commands.ls()
                elif (len(parts)==2):
                    self.commands.lsf(parts[1])
                else:
                    print("more arguments for ls command")
            elif parts[0]=='cp':
                if(len(parts)==3):
                    self.commands.cp(parts[1],parts[2])
                elif (len(parts)==2):
                    print("missing source or destination file operand")
                else:
                    print("more arguments for cp command")
            elif parts[0]=='chmod':
                if(len(parts)==2):
                    self.commands.chmod(parts[1])
                else:
                    print("more arguments for c command")
            elif parts[0]=='cd':
                if(len(parts)==2):
                    self.commands.cd(parts[1])
                elif(len(parts)>2):
                    print("more arguments for cd command")
            elif parts[0]=='wc':
                if(len(parts)==2):
                    self.commands.wc("0",parts[1])
                elif(len(parts)==3):
                    self.commands.wc(parts[2],parts[1])
                elif(len(parts)>3):
                    print("more arguments for wc command")
                else:
                    print("missing operands in wc")
            elif parts[0]=='rm':
                if(len(parts)==2):
                    self.commands.rm(parts[1])
                elif(len(parts)>2):
                    print("more arguments for wc command")
                else:
                    print("missing filename in rm")
            elif parts[0]=='mv':
                if(len(parts)==3):
                    self.commands.mv(parts[1],parts[2])
                elif (len(parts)==2):
                    print("missing source or destination file operand")
                elif(len(parts)>3):
                    print("more arguments for mv command")
                else:
                    print("missing source and destination operand")
            elif parts[0]=='history':
                his=self.history.get_commands()
                if(len(parts)==1):
                    for item in his:
                        print(item)
                else:
                    print("more arguments in history command")
            else:
                print("command not found")
                


if __name__=="__main__":
    d = driver()    
    d.runShell()
