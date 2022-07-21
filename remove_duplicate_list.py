data = [['What is Neem Oil?', 'Neem oil comes from the tree Azadirachta indica, a South Asian and Indian plant common as an ornamental shade tree. It has many traditional uses in addition to its insecticidal properties. For centuries, the seeds have been used in wax, oil, and soap preparations. It is currently an ingredient in many organic cosmetic products too.'], ['What is neem oil?', 'Neem oil derives from the fruits and seeds of the neem tree. These trees grow mainly in the Indian subcontinent.'], ['Composition[edit]', "Azadirachtin is the most well known and studied triterpenoid in neem oil. Nimbin is another triterpenoid which has been credited with some of neem oil's properties as an antiseptic, antifungal, antipyretic and antihistamine.[1]\n"]]
newlist = list()
for i in data:

    if i[0].lower() not in newlist:
        newlist.append(i[0].lower())
    
    if i[1].lower not in newlist:
        newlist.append(i[1].lower())
print(newlist)





