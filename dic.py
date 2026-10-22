# test_dict={'Codingal' :2, 'is' :2, 'best' :2, 'for' :2, 'coding' :1}

# print("The original dictionary- " + str(test_dict))

# k=2

# count=0
# for key in test_dict:
#     if test_dict[key] == k:
#         count+=1

# print("Freqauency of k is- " + str(count))

student_data={
    "id1": {"name": "sara", "class": "V", "subject" :"eng, math, sci"},
    "id2": {"name": "david", "class": "V", "subject" :"eng, math, sci"},
    "id3": {"name": "sara", "class": "V", "subject" :"eng, math, sci"},
    "id4": {"name": "Kanao", "class": "V", "subject" :"eng, math, sci"},

}

result={}
seen_keys=[]

for student_id, details in student_data.items():
    unique_key=(details["name"], details["class"], details["subject"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id]= details

for k, v in result.items():
    print(k, ":", v)