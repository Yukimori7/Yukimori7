import pathlib
import re
import os
import datetime
import time
root = pathlib.Path(__file__).parent.resolve()

def replace_chunk(content, marker, chunk, inline=False):
    r = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = "\n{}\n".format(chunk)
    chunk = "<!-- {} starts -->{}<!-- {} ends -->".format(marker, chunk, marker)
    return r.sub(chunk, content)

def generateProgressBar(progress, progressBarCapacity = 30):
    passedProgressBarIndex = int(progress * progressBarCapacity)
    progressBar = '▓'*passedProgressBarIndex + '░'*(progressBarCapacity - passedProgressBarIndex)
    return progressBar

def yearProgress():
    thisYear = datetime.datetime.now().year
    startTimeOfThieYear = int(time.mktime(time.strptime("{}-01-01 00:00:00".format(thisYear),"%Y-%m-%d %H:%M:%S")))
    endTimeOfThisYear = int(time.mktime(time.strptime("{}-12-31 23:59:59".format(thisYear),"%Y-%m-%d %H:%M:%S")))
    nowTime = int(time.time())
    progressOfThisYear = (nowTime - startTimeOfThieYear) / (endTimeOfThisYear - startTimeOfThieYear)
    progressBarOfThisYear = generateProgressBar(progressOfThisYear)
    return "⏳ Year progress {} {}%  ".format(progressBarOfThisYear, round(progressOfThisYear * 100, 1))

def lifeProgress():
    born = int(time.mktime(time.strptime("1994-06-03 00:00:00","%Y-%m-%d %H:%M:%S")))
    death = int(time.mktime(time.strptime("2076-06-03 00:00:00","%Y-%m-%d %H:%M:%S")))
    nowTime = int(time.time())
    progressOfThisYear = (nowTime - born) / (death - born)
    progressBarOfThisYear = generateProgressBar(progressOfThisYear)
    return "😱 Life progress {} {}%  ".format(progressBarOfThisYear, round(progressOfThisYear * 100, 1))

if __name__ == "__main__":
    readme = root / "README.md"
    readme_contents = readme.open().read()

    progressBar = "{} \n{} \n⏰ Update on {}\n".format(yearProgress(), lifeProgress(), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(progressBar)
    rewritten = replace_chunk(readme_contents, "progress", progressBar)

    readme.open("w").write(rewritten)
