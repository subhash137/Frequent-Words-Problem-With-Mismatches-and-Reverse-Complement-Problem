from itertools import product
def split_kmer(Text,k):
    return [Text[i:i+k] for i in range(len(Text)-k+1)]
def reverse_compliment(Pattern):
    reverse_compliment=""
    for i in list(Pattern):
        if(i=="A"):
            reverse_compliment+="T"
        elif(i=="T"):
            reverse_compliment+="A"
        elif(i=="G"):
            reverse_compliment+="C"
        elif(i=="C"):
            reverse_compliment+="G"
    return reverse_compliment[::-1]
def hamming_distance(String1,String2):
    return sum(1 for i in range(len(String1)) if String1[i]!=String2[i])
def Approximate_pattern_count(Pattern,kmers,d):
    return sum(1 for i in kmers if hamming_distance(Pattern,i)<=d)
def generate_Pattern(k):
    return ["".join(p) for p in product(["A","T","G","C"],repeat=k)]  
def Frequent_words_with_mismatches(Text,k,d):
    count_pattern={}
    output=[]
    Patterns = generate_Pattern(k)
    kmers = split_kmer(Text,k)
    for Pattern in Patterns:
        reverse = reverse_compliment(Pattern)
        count_pattern[Pattern]=Approximate_pattern_count(Pattern,kmers,d)+Approximate_pattern_count(reverse,kmers,d)
    max_Count = max(count_pattern.values())
    output = [Pattern for Pattern in count_pattern if count_pattern[Pattern]==max_Count]
    print(*output,end=' ')
File_name = input()
with open(File_name,'r') as f:
    List = f.readlines()
    Text = List[0].strip()
    k = int((List[1].strip()).split(" ")[0])
    d = int((List[1].strip()).split(" ")[1])
    Frequent_words_with_mismatches(Text,k,d)