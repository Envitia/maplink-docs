"""Fix split code blocks in ogc-services-sdk.md"""

with open(r'c:\maplink\maplink-docs\pages\developers-guide\ogc-services-sdk.md', 'rb') as f:
    content = f.read()

fixes = []

# Fix O1: Consolidate the fragmented describeProcess + executeProcess into one fence
fixes.append(('O1 describeProcess+executeProcess consolidated',
    b'TSLWPSProcessDescriptionType\\* SampleWPSDataSource:: describeProcess\r\n\r\n'
    b'(const char\\* language)\r\n\r\n'
    b'{\r\n\r\n'
    b'if ( !m_isConfigurationValid )\r\n\r\n'
    b'```cpp\r\n'
    b'{\r\n'
    b'```\r\n\r\n'
    b'TSLOWSExceptionReport\\* er = new TSLOWSExceptionReport(1, 0, 0);\r\n\r\n'
    b'TSLOWSException\\* ex = new TSLOWSException("NoApplicableCode", "SampleWPSDataSource has not configured correctly");\r\n\r\n'
    b'er-\\>addException(\\*ex);\r\n\r\n'
    b'ex-\\>destroy();\r\n\r\n'
    b'er-\\>throwException();\r\n\r\n'
    b'```cpp\r\n'
    b'}\r\n'
    b'```\r\n\r\n'
    b'TSLWPSProcessDescriptionType\\* desc = new TSLWPSProcessDescriptionType("1.0.0");\r\n\r\n'
    b'desc-\\>identifier().value("SampleProcess");\r\n\r\n'
    b'```cpp\r\n'
    b'//TODO: Add inputs and output descriptions\r\n\r\n'
    b'return desc;\r\n'
    b'```\r\n\r\n'
    b'```cpp\r\n'
    b'}\r\n\r\n'
    b'TSLWPSExecuteResponse* SampleWPSDataSource::executeProcess\r\n'
    b'```\r\n'
    b'(const TSLWPSExecuteRequest \\*request,\r\n\r\n'
    b'TSLWPSStoreHelper\\* storeHelper,\r\n\r\n'
    b'TSLWPSProgressSink\\* progressSink)\r\n\r\n'
    b'```cpp\r\n'
    b'{\r\n\r\n'
    b'//TODO: Interrogate request for input values\r\n\r\n'
    b'TSLWPSProcessDescriptionType * desc = describeProcess(request->language());\r\n\r\n'
    b'TSLTimeType now;\r\n\r\n'
    b'_time64(&now);\r\n\r\n'
    b'TSLWPSStatusType* sts = new TSLWPSStatusType(now, "Succeeded");\r\n\r\n'
    b'desc->identifier().value("SampleWPSDataSource");\r\n\r\n'
    b'TSLWPSExecuteResponse * res = new TSLWPSExecuteResponse(*desc, *sts);\r\n\r\n'
    b'desc->destroy();\r\n\r\n'
    b'sts->destroy();\r\n\r\n'
    b'//TODO: Add outputs\r\n\r\n'
    b'return true;\r\n\r\n'
    b'}\r\n'
    b'```',
    b'```cpp\r\n'
    b'TSLWPSProcessDescriptionType* SampleWPSDataSource:: describeProcess\r\n\r\n'
    b'(const char* language)\r\n\r\n'
    b'{\r\n\r\n'
    b'if ( !m_isConfigurationValid )\r\n\r\n'
    b'{\r\n\r\n'
    b'TSLOWSExceptionReport* er = new TSLOWSExceptionReport(1, 0, 0);\r\n\r\n'
    b'TSLOWSException* ex = new TSLOWSException("NoApplicableCode", "SampleWPSDataSource has not configured correctly");\r\n\r\n'
    b'er->addException(*ex);\r\n\r\n'
    b'ex->destroy();\r\n\r\n'
    b'er->throwException();\r\n\r\n'
    b'}\r\n\r\n'
    b'TSLWPSProcessDescriptionType* desc = new TSLWPSProcessDescriptionType("1.0.0");\r\n\r\n'
    b'desc->identifier().value("SampleProcess");\r\n\r\n'
    b'//TODO: Add inputs and output descriptions\r\n\r\n'
    b'return desc;\r\n\r\n'
    b'}\r\n\r\n'
    b'TSLWPSExecuteResponse* SampleWPSDataSource::executeProcess\r\n\r\n'
    b'(const TSLWPSExecuteRequest *request,\r\n\r\n'
    b'TSLWPSStoreHelper* storeHelper,\r\n\r\n'
    b'TSLWPSProgressSink* progressSink)\r\n\r\n'
    b'{\r\n\r\n'
    b'//TODO: Interrogate request for input values\r\n\r\n'
    b'TSLWPSProcessDescriptionType * desc = describeProcess(request->language());\r\n\r\n'
    b'TSLTimeType now;\r\n\r\n'
    b'_time64(&now);\r\n\r\n'
    b'TSLWPSStatusType* sts = new TSLWPSStatusType(now, "Succeeded");\r\n\r\n'
    b'desc->identifier().value("SampleWPSDataSource");\r\n\r\n'
    b'TSLWPSExecuteResponse * res = new TSLWPSExecuteResponse(*desc, *sts);\r\n\r\n'
    b'desc->destroy();\r\n\r\n'
    b'sts->destroy();\r\n\r\n'
    b'//TODO: Add outputs\r\n\r\n'
    b'return true;\r\n\r\n'
    b'}\r\n'
    b'```'
))

for name, old, new in fixes:
    found = old in content
    print(f'{name}: found={found}')
    if found:
        content = content.replace(old, new, 1)
    else:
        print(f'  first 80: {old[:80]}')
        print(f'  first 80 found: {old[:80] in content}')

with open(r'c:\maplink\maplink-docs\pages\developers-guide\ogc-services-sdk.md', 'wb') as f:
    f.write(content)
print('ogc-services-sdk.md written')
