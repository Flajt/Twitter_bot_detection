# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import numpy as np

class encoder():
    def __init__(self,special_characters_dic={}):
        """
        Possible setup:
        c=encoder(special_characters_dic={",":69,".":70})# only usefull for words with special_characters, if you don`t need it leave it empty
        words=c.split_words(["my words"])#important
        out=c.on_hot_all(words)#encode all words with special_characters and upper and lower_case characters
        for i in out:
            print(i)
            print("")
        """
        #not really needed
        self.word_dic={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
        self.upper_word_dic={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
        self.general_lower_word_list={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
        self.general_upper_word_list={"A":26,"B":27,"C":28,"D":29,"E":30,"F":31,"G":32,"H":33,"I":34,"J":35,"K":36,"L":37,"M":38,"N":39,"O":40,"P":41,"Q":42,"R":43,"S":44,"T":45,"U":46,"V":47,"W":48,"X":49,"Y":50,"Z":51}
        self.special_letters_dic={"ä":52,"ü":53,"ö":54,"ß":55,"Ä":56,"Ü":57,"Ö":58}
        self.special_characters_dic=special_characters_dic
        self.general_numbers_dic={"1":59,"2":60,"3":61,"4":62,"5":63,"6":64,"7":65,"8":66,"9":67,"0":68}
        self.coder=None



    def coder(self):
        """Return type of the encoder"""
        return self.coder

    def split_words(self,data=[None]):
        """Use a list of words as input and returns a list of lists containing the splitted words"""
        content=[]
        self.data=data
        for i in data:
            liste=list(i)
            content.append(liste)
        return content

    def return_values(self):
        """Return the dictionaries and their content"""
        try:
            return self.word_dic,self.upper_word_dic,self.sepecial_letters_dic,self.special_letters_dic,self.general_numbers_dic,self.general_lower_word_list,self.general_upper_word_list
        except Exception as e:
            return self.word_dic,self.upper_word_dic,self.special_letters_dic,self.general_numbers_dic,self.general_lower_word_list,self.general_upper_word_list

    def create_new_array(self,shape=(26,26),replace=False,replace_with=-1):
        """create a new array with default shape of (26,26)"""
        if replace==False:
            return np.zeros(shape)
        else:
            array=np.zeros(shape)
            for i in range(0,len(array)):
                array[i]=replace_with
            return array

    def on_hot_lower(self,splitted_words, description="basic on_hot method for lower_case characters"):
        """One hot encoder for lower_case characters, needs splitted_words as input list and returns a list of numpy matrices as output. Size default(26,26)"""
        self.coder="on_hot_lower"
        array=self.create_new_array()
        array_storage=[]
        for i in splitted_words:#iterate through every list
            for letter in i:#iterate thorugh every letter in i
                position=self.word_dic[letter]
                index=i.index(letter)
                array[index,position]=1
                array=self.create_new_array(max_word_lenght,26)
            array_storage.append(array)
        return array_storage

    def on_hot_upper(self,splitted_words,max_word_lenght=26):
        """One hot encoder for upper_case characters, needs splitted_words as input list and returns a list of numpy matrices as output. Size default (26,26)"""
        self.coder="on_hot_upper"
        array=self.create_new_array(shape=(max_word_lenght,26))
        array_storage=[]
        for i in splitted_words:#iterate through every list
            for letter in i:#iterate thorugh every letter in i
                position=self.upper_word_dic[letter]
                index=i.index(letter)
                array[index,position]=1
            array_storage.append(array)
            array=self.create_new_array(shape=(max_word_lenght,26))
        return array_storage

    def on_hot(self,splitted_words,max_word_lenght=26):
        """One hot encoder for lower_case and upper_case characters, needs splitted_words as input list and returns a list of numpy matrices as output. Size default (26,52)"""
        self.coder="on_hot_without_special_characters"
        array=self.create_new_array(shape=(max_word_lenght,52))
        array_storage=[]
        for i in splitted_words:#iterate through every list
            for letter in i:#iterate thorugh every letter in i
                if str.isupper(letter)==True:
                    position=self.general_upper_word_list[letter]
                    index=i.index(letter)
                else:
                    position=self.general_lower_word_list[letter]
                    index=i.index(letter)

                array[index,position]=1
            array_storage.append(array)
            array=self.create_new_array(shape=(max_word_lenght,52))
        return array_storage

    def on_hot_all(self, splitted_words,max_word_lenght=26,disable_numbers=False):#all the on_hot* functions uses 0 and 1 to represent the letters
        """Generates a list of arrays of the (default)size (26,56+length of sepecial_characters_dic)"""
        array_storage=[]
        if self.special_characters_dic==True or None or False:
            raise ValueError("Please input a list of special characters to use this function. These dictionary should start by: 69")
        else:
            pass
        self.coder="on_hot_encoder_with special_characters_maybe_memeory_intensiv_so_be_aware"
        if disable_numbers==True:
            #print(type(self.special_characters_dic))
            if len(self.special_characters_dic)>0:
                array=self.create_new_array(shape=(max_word_lenght,58+len(self.special_characters_dic)+2))
            else:
                array=self.create_new_array(shape=(max_word_lenght,58+1))
        else:
            if len(self.special_characters_dic)>0:
                array=self.create_new_array(shape=(max_word_lenght,68+len(self.special_characters_dic)+2))
            else:
                array=self.create_new_array(shape=(max_word_lenght,68+1))
        for i in splitted_words:#iterate through every list
            #print(str(i)+" "+str(len(i))+"\n")
            for letter in i:#iterate thorugh every letter in i
                #print(letter)
                if str.isupper(letter)==True and letter not in self.special_letters_dic and letter not in self.special_characters_dic: #these lines checks in wich dictionary the word is inside and figure out the matrix positions
                    position=self.general_upper_word_list[letter]
                    index=i.index(letter)
                elif str.islower(letter)==True and letter not in self.special_letters_dic and letter not in self.special_characters_dic:
                    position=self.general_lower_word_list[letter]
                    index=i.index(letter)
                elif self.special_characters_dic!=None and letter in self.special_characters_dic:
                    position=self.special_characters_dic[letter]
                    index=i.index(letter)
                elif letter in self.special_letters_dic:
                    position=self.special_letters_dic[letter]
                    index=i.index(letter)
                elif letter in self.general_numbers_dic and disable_numbers==False:
                    position=self.general_numbers_dic[letter]
                    index=i.index(letter)
                else:
                    print("\n The letter:"+letter+" is not known by the programm, please check your sepecial_characters dictionary\n")
                array[index,position]=1
            array_storage.append(array)
            if disable_numbers==True:
                if len(self.special_characters_dic)>0:
                    array=self.create_new_array(shape=(max_word_lenght,58+len(self.special_characters_dic)+2))
                else:
                    array=self.create_new_array(shape=(max_word_lenght,58+1))
            else:
                if len(self.special_characters_dic)>0:
                    array=self.create_new_array(shape=(max_word_lenght,68+len(self.special_characters_dic)+2))#a matrix with the the lenght of all words+ the lenght of the speacial wirds dictionary

                else:
                    array=self.create_new_array(shape=(max_word_lenght,68+1))
        return array_storage

    def short_vector(self, splitted_words, max_array_size=26):# iterate in another way
        """Use it to create word vectors in a smater way"""
        self.coder="An_real_word_vector_algorith_that_uses_the_letter_position_in_a_dictionary"
        storage=[]#create an array storage
        not_found=[]#store the unkown words
        array=self.create_new_array(shape=(max_array_size,1),replace=True)# build an new arry and fill it with -1s then 0s
        array_position=0#set the positon in the array equal to 0; used to move around the array
        if len(self.special_characters_dic)>0:# checks if there are items in these dictionary
            for i in splitted_words:# iterate thorugh the list of splitted words
                for word in i: # iterate through the list of letters
                    if word in self.general_lower_word_list:# now figure out if the letter is in that dictionary
                        array[array_position]=self.general_lower_word_list[word]# and replace these with its number at the given array positon
                        array_position+=1#add one to the positon to move to the next row in the array
                    elif word in self.general_upper_word_list:
                        array[array_position]=self.upper_word_dic[word]
                        array_position+=1
                    elif word in self.special_letters_dic:
                        array[array_position]=self.special_letters_dic[word]
                        array_position+=1
                    elif word in self.general_numbers_dic:
                        array[array_position]=self.general_numbers_dic[word]
                        array_position+=1
                    elif word in self.special_characters_dic:
                        array[array_position]=self.special_characters_dic[word]
                        array_position+=1
                    else:
                        print("This word is not know by the list: "+word)
                        not_found.append(word)
                storage.append(array)
                array_position=0
                array=self.create_new_array(shape=(max_array_size,1),replace=True)
        else:
            for i in splitted_words:
                for word in i:
                    if word in self.general_lower_word_list:
                        array[array_position]=self.general_lower_word_list[word]
                        array_position+=1
                        #print(array)
                    elif word in self.upper_word_dic:
                        array[array_position]=self.upper_word_dic[word]
                        array_position+=1
                        #print(array)
                    elif word in self.special_letters_dic:
                        array[array_position]=self.special_letters_dic[word]
                        array_position+=1
                        #print(array)
                    elif word in self.general_numbers_dic:
                        array[array_position]=self.general_numbers_dic[word]
                        array_position+=1
                        #print(array)
                    else:
                        print("This word is not know by the list: "+word)
                        not_found.append(word)
                        pass
                storage.append(array)
                array_position=0
                array=self.create_new_array(shape=(max_array_size,1),replace=True)
        return storage,not_found

    def dictionary_value_grabber(self, value, dic):
        """Searchs for a spefified value in a dictionary, not a key!"""
        self.coder="Used to grab a value in a dictionary"
        for v in dic.values():
            if v==value:
                return value
            else:
                pass

    def decoder(self, array=[],your_dic_max_value=78):
        """Decodes words that are encoded from the short vector function"""
        word_list=[]
        self.coder="This_is_a_decoder_for_the_short_vector_function!"
        for i in array:
            for i in i:
                print("i:"+str(i))
                if int(i) <=25:# use the max length of the dic to find out wich one to use
                    for key, value in self.general_lower_word_list.items():# iterate through every key and value
                        if value==int(i):#checks if the value is equal to the given input
                            word_list.append(key)# if yes append it
                        else:
                            pass #else move on
                elif int(i) <=51 and int(i)>=25:# same process as above
                    for key, value in self.general_upper_word_list.items():
                        if value==int(i):
                            word_list.append(key)
                        else:
                            pass
                elif int(i) <=58 and int(i)>=52:
                    for key, value in self.special_letters_dic.items():
                        if value==int(i):
                            word_list.append(key)
                        else:
                            pass
                elif int(i) <=68 and int(i)>=59:
                    for key, value in self.general_numbers_dic.items():
                        if value==int(i):
                            word_list.append(key)
                        else:
                            pass
                elif int(i) <=max_value and int(i)>=69:
                    for key, value in self.special_characters_dic.items():
                        if value==int(i):
                            word_list.append(key)
                        else:
                            pass
        return "".join(word_list) #create a real string with the join method


    def find_letter_in_dics(self,letter):
        """Finds letters in all dictionaries"""
        if str.isupper(letter)==True and letter not in self.special_letters_dic and letter not in self.special_characters_dic: #taken from above
            position=self.general_upper_word_list[letter]
        elif str.islower(letter)==True and letter not in self.special_letters_dic and letter not in self.special_characters_dic:
            position=self.general_lower_word_list[letter]
        elif self.special_characters_dic!=None and letter in self.special_characters_dic:
            position=self.special_characters_dic[letter]
        elif letter in self.special_letters_dic:
            position=self.special_letters_dic[letter]
        elif letter in self.general_numbers_dic:
            position=self.general_numbers_dic[letter]
        return position


    def binary_encoder(self,splitted_word_array=[],T=False):
        """Encodes words in binary format, no decoder actually planned, if needed it will be added! """
        word_list=[]
        position=1
        self.coder="A_Binary_encoder_for_words"
        for words in splitted_word_array:
            if T==False and len(self.special_characters_dic)==0:
                array=self.create_new_array(shape=(2,68),replace=True)
            elif T==True and len(self.special_characters_dic)==0:
                array=self.create_new_array(shape=(68,2),replace=True)
            else:
                T==False
            if T==False and len(self.special_characters_dic)>0:
                array=self.create_new_array(shape=(2,68+len(self.special_characters_dic)+1),replace=True)
            elif T==True and len(self.special_characters_dic)>0:
                array=self.create_new_array(shape=(68+len(self.special_characters_dic)+1,2),replace=True)
            else:
                T==False
            for i in words:
                p=self.find_letter_in_dics(i)
                if len(self.special_characters_dic)>0:
                    array[0,p]=1
                    array[1,p]=position
                    position+=1
                elif len(self.special_characters_dic)==0:
                    array[p,0]=1
                    array[p,1]=position
                    position+=1
                else:
                    raise ValueError("Something is wrong with your special_characters_dic")
            word_list.append(array)
        return word_list
