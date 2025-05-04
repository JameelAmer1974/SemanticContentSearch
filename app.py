from flask import Flask, render_template, request,jsonify
from summary import get_summary
from waitress import serve
from generte_text import generate_text
app = Flask(__name__)

print("app name",__name__)
@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/summary', methods=["GET","POST"])
def summary():
    documet_content="""
    ذكرت وكالة الأنباء المحلية (جي.إن.إس) أن جماعة "جيش محمد" المتشددة أعلنت مسؤوليتها عن الهجوم. لكن ما هي منطقة كشمير المتنازع عليها بين الهند وباكستان؟ خلال العقود الست الماضية ظلت منطقة كشمير القريبة من جبال الهيمالايا محل نزاع بين الهند وباكستان. الجنة الملعونة دموع الفقراء في كشمير لماذا يلجأ الناس إلى أضرحة الصوفيين في "كشمير الهندية"؟ بالصور الطفولة المسروقة في كشمير فمنذ تقسيم الهند وقيام باكستان عام 1947 وقعت حربان بين البلدين حول منطقة كشمير ذات الأغلبية المسلمة والتي يطالب البلدان بالسيادة عليها. وتعد كشمير اليوم واحدة من أكثر المناطق المدججة بالسلاح في العالم، في ما تدير الصين أجزاء من الإقليم. تسلسل زمني لأهم الأحداث في كشمير' وزارة الدفاع الأمريكية تقول إن الفضلي كان أحد قادة تنظيم القاعدة القلائل الذين أُبلغوا مسبقا بشأن هجمات 9/11 في نيويورك عام  وقال المرصد السوري لحقوق الإنسان المعارض ، ومقره بريطانيا ، إن الغارات الجوية التي شنها التحالف الدولي بقيادة الولايات المتحدة استهدفت مواقع لتنظيم " الدولة الإسلامية " في محافظة دير الزور .وأضاف المرصد أن الغارات أسفرت أيضا عن تدمير عدد من المنازل في المنطقة . وقال رامي عبد الرحمن ، مدير المرصد ، لبي بي سي إن الضربات الجوية استهدفت أيضا مواقع للتنظيم في بلدة تل أبيض . مواضيع قد تهمك نهاية وأضاف أن " الغارات دمرت أيضا عددا من المباني في منطقة تل ابيض " ، بحسب ما نقلته وكالة الأنباء السورية الرسمية ( سانا ) . ولم يتسن التأكد من صحة هذه الأنباء من مصادر مستقلة . وكان المرصد قد قال في وقت سابق إن طائرات التحالف شنت سلسلة غارات جوية على مناطق خاضعة لسيطرة المعارضة المسلحة في مدينة الرقة ، شمالي سوريا ، ما أسفر عن مقتل أكثر من 50 شخصا ، بينهم نساء وأطفال . وفي وقت لاحق ، قال المرصد إن الطيران الحربي السوري شن غارات على مواقع لمسلحي المعارضة في ريف دمشق ، ردا على هجوم شنه مسلحو المعارضة على بلدة عين العرب ( كوباني ) ، الواقعة على الحدود مع تركيا . وكانت القوات الحكومية السورية قد تمكنت من استعادة السيطرة على عدة مناطق في شمال شرقي البلاد ، بعد معارك عنيفة مع مسلحي المعارضة ، الذين يسيطرون على مساحات واسعة من الأراضي السورية . وقالت وكالة رويترز للأنباء إن الجيش السوري وحلفاءه شنوا سلسلة من الهجمات الجوية على المناطق التي تسيطر عليها المعارضة . ونقلت الوكالة عن مصدر عسكري سوري قوله إن " وحدات حماية الشعب الكردية " قصفت مواقع للمسلحين الأكراد في محيط بلدة كفر زيتا ، التي تقع على بعد نحو 50 كيلومترا إلى الشمال الشرقي من العاصمة السورية دمشق .
    """
    print("Form Data:", request.form.to_dict())
    print("Raw Data:", request.data)
    #print("JSON Data:", request.json)
    # Get JSON data
    #data = request.get_form()
    document_content1 = request.form.get("document_content")
    print("content:: ", document_content1)
    #documet_content=request.form.get('document_content')
    doc_summary = get_summary(document_content1)
    #print(documet_content)
    return render_template('summary.html',
                           summary=doc_summary)


@app.route('/generate_answer', methods=["GET","POST"])
def generate_answer():
    documet_content="""
    الحرب السورية
     """
    print("Form Data:", request.form.to_dict())
    print("Raw Data:", request.data)
    #print("JSON Data:", request.json)
    # Get JSON data
    #data = request.get_form()
    question = request.form.get("document_content")
    print("content:: ", question)
    #documet_content=request.form.get('document_content')
    generated_text = generate_text(question)
    #print(documet_content)
    return render_template('summary.html',
                           summary=generated_text)



if __name__ == "app":
    # Run Flask app with Waitress in production
    print("Starting server on http://0.0.0.0:8000")
    serve(app, host="0.0.0.0", port=8000)