from client import FarmToDoorTraceableProduceColdchainAuditClient

def main():
    client = FarmToDoorTraceableProduceColdchainAuditClient()
    res = client.audit_produce_traceability('PLK_SCAN_BELLPEPPER_22')
    print('Crop: ' + res['crop_name'] + ' from ' + res['farm_source'])
    print('Harvest: ' + res['harvest_timestamp'] + ' | Grade: ' + res['pan_scanned_quality_grade'])
    print('Pesticides: ' + str(res['chemical_pesticide_residue_ppm']) + ' ppm | Ozone Washed: ' + str(res['ozone_wash_and_sanitization_certified']))

if __name__ == '__main__':
    main()
