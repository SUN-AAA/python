s1 = 'Kang Young Min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong_Yun'

ns1 = s1.strip('').upper().replace(' ','')
s1_n = ns1.count("N")

ns2 = s2.strip('').replace('-','').upper().replace(' ','')
s2_n = ns2.count("N")

ns3 = s3.strip('').upper().replace(' ','')
s3_n = ns3.count("N")

ns4 = s4.strip('').replace('_','').upper().replace(' ','')
s4_n = ns4.count("N")

print(f"{s1.strip('')} is modified to {ns1}")
print(f"{s2.strip('')} is modified to {ns2}")
print(f"{s3.strip('')} is modified to {ns3}")
print(f"{s4.strip('')} is modified to {ns4}")

print(ns1,":",s1_n,"N(s) appear")
print(ns2,":",s2_n,"N(s) appear")
print(ns3,":",s3_n,"N(s) appear")
print(ns4,":",s4_n,"N(s) appear")