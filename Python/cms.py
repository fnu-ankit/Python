import requests
import json

url = "https://webpricer.cms.gov/api/ipps-pricer/v2/price-claim"

payload = json.dumps({
  "claimData": {
    "providerCcn": "440048",
    "coveredCharges": "50000.00",
    "coveredDays": "20",
    "diagnosisRelatedGroup": "871",
    "dischargeDate": "2024-06-28",
    "lengthOfStay": "7",
    "lifetimeReserveDays": 0,
    "nationalDrugCodes": [None],
    "reviewCode": "00"
  },
  "providerData": {
    "cbsaActualGeographicLocation": "32820",
    "costOfLivingAdjustment": 1,
    "countyCode": "47157",
    "effectiveDate": "2024-01-25",
    "fiscalYearBeginDate": "2023-10-01",
    "hospitalQualityIndicator": "1",
    "intermediaryNumber": "10311",
    "medicarePerformanceAdjustment": 0,
    "operatingCostToChargeRatio": 0.203,
    "providerCcn": "440048",
    "providerType": "00",
    "specialWageIndex": 0,
    "stateCode": "44",
    "supplementalWageIndex": 0.8329,
    "supplementalWageIndexIndicator": "1",
    "waiverIndicator": "N",
    "bedSize": 791,
    "bundleModel1Discount": 0,
    "capitalCostToChargeRatio": 0.017,
    "capitalExceptionPaymentRate": 0,
    "capitalIndirectMedicalEducationRatio": 0.1188,
    "capitalPpsPaymentCode": "C",
    "hacReductionParticipantIndicator": "Y",
    "hrrAdjustment": 0.9921,
    "hrrParticipantIndicator": "1",
    "internsToBedsRatio": 0.0735,
    "lowVolumeAdjustmentFactor": 0,
    "medicaidRatio": 0.2589,
    "oldCapitalHoldHarmlessRate": 0,
    "passThroughAmountForAllogenicStemCellAcquisition": 11.58,
    "passThroughAmountForDirectMedicalEducation": 100.34,
    "passThroughAmountForOrganAcquisition": 24.51,
    "passThroughTotalAmount": 124.85,
    "ppsFacilitySpecificRate": 2784.45,
    "supplementalSecurityIncomeRatio": 0.0752,
    "uncompensatedCareAmount": 533.37,
    "vbpAdjustment": 0,
    "vbpParticipantIndicator": "N"
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
