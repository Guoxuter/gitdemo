import re

class Animal:
    ''' 用来存储动物类型 '''
    def __init__(self, name, features=[], labels=[]):
        self._name = name
        self._features = features
        self._labels = labels
        self._message = None

    def get_name(self):
        return self._name

    def get_features(self):
        return self._features
    
    def get_labels(self):
        return self._labels
    
    def update_name(self, name):
        self._name = name

    def update_features(self, features):
        self._features = features

    def update_labels(self, label):
        self._labels = label
    
    def append_feature(self, feature):
        self._features.append(feature)
    
    def append_label(self, label):
        self._labels.append(label)
    
    def remove_feature(self, feature):
        if feature in self._features:
            self._features.remove(feature)
        else:
            print(f"feature {feature} does not exist.")
    
    def remove_label(self, label):
        if label in self._labels:
            self._features.remove(label)
        else:
            print(f"label {label} does not exist.")
    
    def has_feature(self, feature):
        return feature in self._features
    
    def has_label(self, label):
        return label in self._labels
    
    def record(self, message):
        if self._message is None:
            self._message = message
        else:
            self._message += message

    def __str__(self):
        if self.get_name() == "":
            return f'The animal name was not successfully identified.\nfeatures:\t{self.get_features()}\nlabels:\t{self.get_labels()}\n\nmessage:{self._message}\n\n'
        return f'Successfully identified.\nname:\t{self.get_name()}\nfeatures:\t{self.get_features()}\nlabels:\t{self.get_labels()}\n\nmessage:{self._message}\n\n'

class Identify:
    ''' 根据规则识别动物 '''

    def __init__(self, Animal):
        self._Animal = Animal
        rules = Rules()
        self._Rulelist = rules.get_rules()
        ''' Rulelist中的元素为 dic，其中包含一条规则的信息
        键包括：'IF_feature'，'IF_label', 'THEN_feature'，'THEN_label', 'THEN_name'
        值为相对应的信息列表
        '''
        self.judge()  # 根据规则对 Animal 的 feature 和 label 进行更新
        self.identify()  # 识别动物

    def judge(self):
        '''根据规则对 Animal 的 feature 和 label 进行递归更新'''
        features = self._Animal.get_features()
        labels = self._Animal.get_labels()

        RECURSE = False
        for Rule in self._Rulelist:
            if Rule['THEN_name'] != []:  # 如果是识别语句，则跳过
                continue

            MATCH = True
            for IF_feature in Rule['IF_feature']:
                if IF_feature not in features:
                    MATCH = False
            for IF_label in Rule['IF_label']:
                if IF_label not in labels:
                    MATCH = False
            if MATCH:
                for THEN_feature in Rule['THEN_feature']:
                    if THEN_feature not in self._Animal.get_features():
                        self._Animal.append_feature(THEN_feature)
                        IF_statement = [feature for feature in Rule['IF_feature']] + [label for label in Rule['IF_label']]
                        self._Animal.record(f'{IF_statement} -> {THEN_feature}\n')
                        RECURSE = True
                for THEN_label in Rule['THEN_label']:
                    if THEN_label not in self._Animal.get_labels():
                        self._Animal.append_label(THEN_label)
                        IF_statement = [feature for feature in Rule['IF_feature']] + [label for label in Rule['IF_label']]
                        self._Animal.record(f'{IF_statement} -> {THEN_label}\n')
                        RECURSE = True
        if RECURSE:  # 如果Animal的状态有更新，则递归
            self.judge()

    def identify(self):
        '''根据规则识别 Animal '''
        features = self._Animal.get_features()
        labels = self._Animal.get_labels()

        for Rule in self._Rulelist:
            if Rule['THEN_name'] == []:
                continue

            MATCH = True
            for IF_feature in Rule['IF_feature']:
                if IF_feature not in features:
                    MATCH = False
            for IF_label in Rule['IF_label']:
                if IF_label not in labels:
                    MATCH = False
            if MATCH:
                name = Rule['THEN_name'][0]
                self._Animal.update_name(name)
                IF_statement = [feature for feature in Rule['IF_feature']] + [label for label in Rule['IF_label']]
                self._Animal.record(f'{IF_statement} -> {name}\n')
                break


RULESPATH = 'AnimalIdf\IdentifyRules.txt'


class Rules:

    def __init__(self, rulespath=RULESPATH):
        self._rulespath = RULESPATH
        self._rules = self.read_rules()

    def get_rules(self):
        return self._rules
        
    def read_rules(self):
        ''' 读取rulespath进行规则读取 '''
        with open(self._rulespath, 'r', encoding='utf-8') as lines:
            Rulelist = []

            for line in lines:
                split_by_THEN = re.split('THEN', string=line)
                IF_statement = split_by_THEN[0].strip()  # split_by_THEN的第一个元素是IF语句段
                THEN_statement = split_by_THEN[1].strip()   # split_by_THEN的第二个元素是THEN语句段

                dic = {}
                # IF_feature代表IF语句中的feature判断，其余同
                IF_feature = re.findall(re.compile(r'[(](.*?)[)]'), IF_statement)
                IF_label = re.findall(re.compile(r'[\[](.*?)[\]]'), IF_statement)

                THEN_feature = re.findall(re.compile(r'[(](.*?)[)]'), THEN_statement)
                THEN_label = re.findall(re.compile(r'[\[](.*?)[\]]'), THEN_statement)
                THEN_name = re.findall(re.compile(r'[\{](.*?)[\}]'), THEN_statement)
                dic['IF_feature'] = IF_feature
                dic['IF_label'] = IF_label
                dic['THEN_feature'] = THEN_feature
                dic['THEN_label'] = THEN_label
                dic['THEN_name'] = THEN_name

                Rulelist.append(dic)

        return(Rulelist)
    
    def add_rules(self):
        with open(self._rulespath, 'r', encoding='utf-8') as lines:
            pass

    def delete_rules(self):
        with open(self._rulespath, 'r', encoding='utf-8') as lines:
            pass


def AnimalIdentify(features=[], labels=[]):
    '''调用Animal、Identify进行识别'''
    animal = Animal(name="", features=features, labels=labels)
    Identify(animal)
    return animal


class TestCases:
    def input_msg(sentence):
        fp = re.compile(r'features:(.*)\n')
        lp = re.compile(r'labels:(.*)')
        f=fp.findall(sentence)[0].split(',')
        l=lp.findall(sentence)[0].split(',')
        for i in range(len(f)):
            f[i]=f[i].strip(' ')
            f[i]=f[i].replace('\r' , '')
            
        for j in range(len(l)):
            l[j]=l[j].strip(' ')
            l[j]=l[j].replace('\r' , '')
        return (f,l)
        
    def test(f,l):
        features = ["canine teeth", "paws", "binocular vision", "yellowish brown", "black stripe"]
        labels = ["mammal"]
        features=f
        labels=l
        
        return AnimalIdentify(features, labels)


if __name__ == "__main__":
    TestCases.test(1,2)
