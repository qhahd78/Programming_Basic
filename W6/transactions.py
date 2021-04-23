# 의용메카트로닉스공학과 20195277 하유민
print("의용메카트로닉스공학과 20195277 하유민")

def save_transaction(price, credit_card, description):
    file = open("transactions.txt", "a")
    file.write("%07d%16s%16s\n" % (price * 100, credit_card, description))
    file.close() 