from django.db import models
from django.conf import settings

# Create your models here.

# 정기 예금 API
class DepositProducts(models.Model):    
    fin_prdt_cd = models.TextField(unique=True) # 금융 상품 코드
    kor_co_nm = models.TextField()  # 금융 회사 명
    fin_prdt_nm = models.TextField()    # 금융 상품 명
    etc_note = models.TextField()   # 기타 유의사항
    join_deny = models.IntegerField()   # 가입 제한
    join_member = models.TextField()    # 가입 대상
    join_way = models.TextField()   # 가입 방법
    spcl_cnd = models.TextField()   # 우대 조건

class DepositOptions(models.Model):
    product = models.ForeignKey("financial_products.DepositProducts", on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()    # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)    # 저축 금리 유형명
    intr_rate = models.FloatField()     # 저축 금리
    intr_rate2 = models.FloatField()    # 최고 우대 금리
    save_trm = models.IntegerField()    # 저축 기간(단위: 개월)

# 적금 API
class SavingProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융 상품 코드
    kor_co_nm = models.TextField()              # 금융 회사 명
    fin_prdt_nm = models.TextField()            # 금융 상품 명
    join_way = models.TextField()               # 가입 방법
    spcl_cnd = models.TextField()               # 우대 조건
    join_deny = models.IntegerField()           # 가입 제한
    join_member = models.TextField()            # 가입 대상
    etc_note = models.TextField()               # 기타 유의사항

class SavingOptions(models.Model):
    product = models.ForeignKey("financial_products.SavingProducts", on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()    # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)    # 저축 금리 유형명
    rsrv_type_nm = models.TextField()	# 적립 유형명
    intr_rate = models.FloatField()     # 저축 금리
    intr_rate2 = models.FloatField()    # 최고 우대 금리
    save_trm = models.IntegerField()    # 저축 기간(단위: 개월)


################# 포트폴리오 모델 ####################

class Answers(models.Model):    # 답변 기록
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    q1_expected_goal_amount = models.IntegerField() # 목표를 달성하기 위해 필요한 예상 금액
    q2_goal_duration = models.IntegerField()   # 목표를 언제까지 달성하고 싶으신가요?
    q3_income_source = models.CharField(max_length=100) # 현재 소득은 어떻게 얻고 있나요?
    q4_emergency_fund_status = models.CharField(max_length=100)   # 예기치 않은 상황에 대비한 비상 자금이 마련되어 있나요?
    q5_investment_priority = models.CharField(max_length=100) # 투자할 때 더 중요하게 여기는 것
    q6_safety_or_liquidity = models.CharField(max_length=100) # 안전성과 유동성 중 중요한 부분
    q7_household_status = models.CharField(max_length=100)    # 가계 상황
    # q8_average_monthly_income = models.IntegerField()  # 평균적인 월 수입

class FinancialProduct(models.Model):  # 위험도에 따른 분류
    answer = models.OneToOneField(Answers, on_delete=models.CASCADE, primary_key=True)
    
    # 위험도에 따른 포폴 구성 비율 저장 필드
    low_ratio = models.FloatField()         # 저
    med_low_ratio = models.FloatField()     # 중저
    med_ratio = models.FloatField()         # 중
    med_high_ratio = models.FloatField()    #중고
    high_ratio = models.FloatField()        #고 

    # 자산 유형(저축 / 투자)에 따른 포폴 구성 비율 저장 필드
    saving_ratio = models.FloatField()    # 투자 비율
    inv_ratio = models.FloatField()       # 저축 비율

    # 자산 유형(투자 상품 내)에 따른 포폴 구성 비율 저장 필드
    dom_stock_ratio = models.FloatField()   # 국내 주식형
    int_stock_ratio = models.FloatField()   # 해외 주식형
    bond_ratio = models.FloatField()        # 채권형
    alt_invest_ratio = models.FloatField()  # 대안투자

    # 자산 유형(저축 상품 내)에 따른 포폴 구성 비율 저장 필드
    inst_save_ratio = models.FloatField()   # 적금/정기예금
    reg_save_ratio = models.FloatField()    # 보통예금
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

################# 환률 모델 ####################
class ChangeMoney(models.Model):
    cur_unit = models.CharField(max_length=50)          # 통화코드
    ttb = models.CharField(max_length=50)               # 전신환 매입율, 은행이 고객으로부터 외화를 살 때 적용하는 환율 (고객 입장에서 외화를 팔 때).
    tts = models.CharField(max_length=50)               # 전신환 매도율, 은행이 고객에게 외화를 팔 때 적용하는 환율 (고객 입장에서 외화를 살 때).
    deal_bas_r = models.CharField(max_length=50)        # 매매기준율, 일반적으로 사용하는 환율.
    # bkpr = models.CharField(max_length=50)              # 장부가격
    # yy_efee_r = models.CharField(max_length=50)
    # ten_dd_efee_r = models.CharField(max_length=50)
    # kftc_bkpr = models.CharField(max_length=50)
    # kftc_deal_bas_r = models.CharField(max_length=50)
    cur_nm = models.CharField(max_length=50)            # 국가/통화명