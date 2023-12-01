
from django.shortcuts import render
from django.http import HttpResponse
from .textclassification import classifier
from django.views.decorators.csrf import csrf_exempt
from .labels import CANDIDATE_LABELS


def index(request):
    return render(request,"index.html")

@csrf_exempt
def textclassifier(request):
    if request.method == 'POST':
        sequence = request.POST.get('sequence', '')
        candidate_labels = CANDIDATE_LABELS
        payload = {"inputs": sequence, "parameters": {"candidate_labels": candidate_labels}}
        results = classifier(payload, candidate_labels)
        
        # print("API Response:", results)
        
        if 'scores' in results and 'labels' in results:
            max_index = results['scores'].index(max(results['scores']))
            label_with_highest_percentage = results['labels'][max_index]
            highest_percentage = results['scores'][max_index]

            return render(request, 'result.html', {'label': label_with_highest_percentage, 'percentage': highest_percentage, 'sequence': sequence})
        else:            
            error_message = "Invalid response format from the API"
            return render(request, 'error.html', {'error_message': error_message})
        
    return render(request, 'textclassification.html')