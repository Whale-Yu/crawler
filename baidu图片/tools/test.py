# from translate import Translator
#
# keyword_eng = Translator(from_lang="Chinese", to_lang="English").translate('看电视吧的角色')
# print(keyword_eng)

from faker import Faker

faker = Faker()     # locale='zh_CN'
ua = faker.user_agent()
name = faker.name()


