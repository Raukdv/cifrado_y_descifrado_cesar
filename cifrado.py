class Cifrado():
    #Init the class values - You just need two in this case
    def __init__(self, **kwargs):
        if 'value' not in kwargs:
            self.text = None
        else: 
            self.text = kwargs.get('value')

        if 'displacement' not in kwargs:
            self.displacement = None
        else: 
            self.displacement = kwargs.get('displacement')  
    
    #Cranky Validator in __init__ method
    #In this case we're using only letters, 
    #If a special number or character appears our encryption will not happen in the correct way.
    #Take in count maybe you want to validate empty inputs.
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, value):
        if isinstance(value, int):
            raise ValueError("Int values are not allowed")
        elif isinstance(value, str) and value.isalpha() == False:
            raise ValueError("Only letters in str are allowed")   
        else:
            pass
            
        self._text = value

    #This will do the cesar's process
    #Iterate on each letter to reposition it according to our displacement.
    def cifra_cesar(self):
        #Our alphabet
        abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuwxyz"
        #Our container to return
        cifrad=""
        for c in self.text:

            if c in abc:
                cifrad += abc[(abc.index(c)+self.displacement)%(len(abc))]
            else:
                cifrad+=c
        
        return cifrad
    
    #This will decrypt the cease value according to the assigned offset.
    def descifra_cesar(self, value):
        abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuwxyz"
        cifrad = ''
        for letter in value:
            value_to_check = abc.find(letter) - self.displacement
            index_value = int(value_to_check) % len(abc)
            cifrad = cifrad + str(abc[index_value])
        
        return cifrad

    def output(self):
        cifrado = self.cifra_cesar()
        descifrado = self.descifra_cesar(cifrado)
        print(f'Valor cifrado: {cifrado}')
        print(f'Valor descifrado: {descifrado}')
        
object_loco = Cifrado(value='admin', displacement=3)
object_loco.output()