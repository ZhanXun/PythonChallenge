import string

s1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
s2 = ""
alpha1 = "abcdefghijklmnopqrstuvwxyz"
alpha2 = "cdefghijklmnopqrstuvwxyzab"
for c1 in s1:
	count = 0
	c1_is_alpha = False
	for a in alpha1:
		if a == c1:
			s2 = s2 + alpha2[count]
			c1_is_alpha = True
		count +=1
	if not c1_is_alpha:
		s2 = s2 + c1
print s2

tran =  string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
print string.translate(s1, tran)
