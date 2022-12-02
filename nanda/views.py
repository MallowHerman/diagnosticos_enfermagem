from django.shortcuts import render

diagnosticos = [
    {
        'diagnostico': 'Nutrição desequilibrada: menor do que as necessidades corporais',
        'definicao': 'Ingestão de nutrientes insuficiente para satisfazer às necessidades metabólicas.',
        'carateristicas': ['Alteração no paladar', 'Aversão a alimento', 'Cavidade oral ferida', 'Cólica abdominal'],
    },
    {
        'diagnostico': 'Nutrição desequilibrada: menor do que as necessidades corporais',
        'definicao': 'Ingestão de nutrientes insuficiente para satisfazer às necessidades metabólicas.',
        'carateristicas': ['Alteração no paladar', 'Aversão a alimento', 'Cavidade oral ferida', 'Cólica abdominal'],
    },
    {
        'diagnostico': 'Nutrição desequilibrada: menor do que as necessidades corporais',
        'definicao': 'Ingestão de nutrientes insuficiente para satisfazer às necessidades metabólicas.',
        'carateristicas': ['Alteração no paladar', 'Aversão a alimento', 'Cavidade oral ferida', 'Cólica abdominal'],
    },
    {
        'diagnostico': 'Nutrição desequilibrada: menor do que as necessidades corporais',
        'definicao': 'Ingestão de nutrientes insuficiente para satisfazer às necessidades metabólicas.',
        'carateristicas': ['Alteração no paladar', 'Aversão a alimento', 'Cavidade oral ferida', 'Cólica abdominal'],
    },
    {
        'diagnostico': 'Nutrição desequilibrada: menor do que as necessidades corporais',
        'definicao': 'Ingestão de nutrientes insuficiente para satisfazer às necessidades metabólicas.',
        'carateristicas': ['Alteração no paladar', 'Aversão a alimento', 'Cavidade oral ferida', 'Cólica abdominal'],
    },
    {
        'diagnostico': 'Nutrição desequilibrada: menor do que as necessidades corporais',
        'definicao': 'Ingestão de nutrientes insuficiente para satisfazer às necessidades metabólicas.',
        'carateristicas': ['Alteração no paladar', 'Aversão a alimento', 'Cavidade oral ferida', 'Cólica abdominal'],
    },
    {
        'diagnostico': 'Nutrição desequilibrada: menor do que as necessidades corporais',
        'definicao': 'Ingestão de nutrientes insuficiente para satisfazer às necessidades metabólicas.',
        'carateristicas': ['Alteração no paladar', 'Aversão a alimento', 'Cavidade oral ferida', 'Cólica abdominal'],
    },
    {
        'diagnostico': 'Nutrição desequilibrada: menor do que as necessidades corporais',
        'definicao': 'Ingestão de nutrientes insuficiente para satisfazer às necessidades metabólicas.',
        'carateristicas': ['Alteração no paladar', 'Aversão a alimento', 'Cavidade oral ferida', 'Cólica abdominal'],
    }
]

def index(request):
    context = {
        'diagnosticos': diagnosticos
    }
    return render(request, 'nanda/index.html', context)

