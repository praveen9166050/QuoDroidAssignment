from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from robot import run

@csrf_exempt
def execute_tests(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
    data = json.loads(request.body.decode())
    tests = data.get('tests', [])
    
    # Create a Robot Framework test script dynamically
    with open('./tests/dynamic_test.robot', 'w') as file:
        file.write(f"""*** Settings ***\nLibrary    SeleniumLibrary\n\n*** Test Cases ***\n""")
        for test in tests:
            title = test.get('title')
            steps = test.get('steps')
            file.write(f"""{title}\n""")
            for step in steps:
                file.write(f"    {step}\n")
                # file.write('    ' + ' '.join(step.split(' ')[0:-1]) + f'    {step.split(' ')[-1]}\n')

    # Execute the test case using Robot Framework
    result = run('./tests/dynamic_test.robot', outputdir='./results')
    
    return JsonResponse({'The number of test cases failed': result})