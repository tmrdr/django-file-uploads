from django.shortcuts import render, redirect

# Create your views here.
def index(request):
  if request.method == "GET":
    return render(request, 'uploader/index.html')
  if request.method == "POST":
    srt_file = request.FILES['srt_file']
    handle_uploaded_file(srt_file)
    return redirect('index')

def handle_uploaded_file(file):
  with open('out_test', 'wb+') as destination:
    for chunk in file.chunks():
      destination.write(chunk)
  translate_out_test('out_test')

def translate_out_test(out_test):
  filename = "out_test"
  my_file = open(filename)
  out = open('output.js', 'w')
  print("var SUBTITLES = [")
  out.write("var SUBTITLES = [" + "\n")
  counter = 0
  for line in my_file:
    line = line.strip()
    # print(counter)
    if counter == 1:
      print("{")
      out.write(("{" + "\n"))
      print("  " +  "duration: " + "\"" + line + "\",")
      out.write("  " +  "duration: " + "\"" + line + "\"," + "\n")
    elif counter == 2:
      print("  " + "line1: " + "\"" + line + "\",")
      out.write("  " + "line1: " + "\"" + line + "\"," + "\n")
    elif counter == 3:
      if line == "":
        print("  " +  "line2: " + "\"" + "\"" + ",")
        out.write("  " +  "line2: " + "\"" + "\"" + "," + "\n")
        counter = 5
      else:
        print("  " +  "line2: " + "\"" + line + "\",")
        out.write("  " +  "line2: " + "\"" + line + "\"," + "\n")
      print("},")
      out.write("}," + "\n")
    elif counter > 4:
      counter = 0
    counter += 1
  print("];")
  out.write("];" "\n")
  out.close()
