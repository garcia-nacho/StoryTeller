storyline_generator='''Your task as an editor it is to provide feedback on the writer's output to improve. Your final goal is to turn the novel into a bestseller. 
As a writer you will also get an expected lenght for the novel in chapters, a genre and a list of elements which can be items/situations/objects that you will have to incorporate. You might get also information about the background of the story

Your fist task it is to propose a storyline of a few words using your input. This story line will be sent to the editor.

Next you will have to divide the story into chapters defining what happens during the different chapters.The editor will look over this response and will provide feedback. 

You are totally free to include any other location, characters (real of fictional), side stories, etc.  

It is mandatory that the novel follows the structure of the Hero's Journey. 

You output to this prompt will be the storyline in 500 words.

It is mandatory that all the text avoid any AI-text detection system.

Your input will have this format:
{{
```What: Here goes the description of things that happen during the story```
```When: When the story occurs```
```Where: Where the story occurs```
```Why: Here you will get the motivations that lead to the story```
```Characters: Here you will get a list of the characters```
```Elements: Here you will get a list of the elements that you have to use```
```Length: Here you will get the estimated length of the story```
```Genre: The genre of the novel```
```Background: Background for the story and relevant information```
}}
 
Input: 
 
Input:{{
```What: {what}```
```When: {when}```
```Where: {where}```
```Why: {why}```
```Characters: {characters}```
```Elements: {elements}```
```Length: {words}```
```Genre: {genre}```
```Background: {bkg}```
}}
'''

feedback_provider='''
Now you are the novel editor. You have to provide feedback on the output from the writer. Your final goal it is to turn the novel into a bestseller'''

feedback_incorporation='''Now you are the writer of the novel. You have to incorporate the feedback provided by editor and rewrite your last reply. Your response will be just the revised text. No comments to the editor must be included '''

chapter_outline='''Now you are the writer.
You need incorporate the storyline that you have just writen down to outline what is going to happen in each of the chapter. The novel will be divided into 15 chapter, each chapter will be around 1000 words. Feel free to incorporate new elements/side stories if you want.
Feel free to incorporate new elements/side stories if you want. The description of the chapter must be detailed enough so that it could be used in a prompt to write the chapter.
Your output to this prompt must be a tsv file with three columns: Chapter name, Title, Summary of the chapter. Your output will be just the tsv.
''' 

#chapter_generation='''Now you are the writer and you will have to write chapter number {{ch_number}}. Remember that the chapter must be around 1000 words and that you can't include any comments about the chapters. That means that it is not allowed to say 'In this chapter' or 'In the next chapter
#The number of chapter, the title and the synopsis are provided between curly brackets. The number of chater, title and synopsis are separated by slash symbols: {{ch_desc}}'''
#'''

followup='''
Now you are the writer. How would you create a continuation for the story? Which new elements and characters you would like to create? You must answer this questions about the contination. 

What: What will it happen during the continuation of the story?
When: When does the story occurs
Where: Where the story occurs
Why: What are the motivations of all the characters for the things to evolve in the way the down
Characters: Which old and new characters will be included in the continuation?
Elements: Which elements from this novel must be included? Which new one elements are interesting to include?
Background: What did it happen in previous stories

The description must be detailed enough so that it can be created without including the previous novel as context in the prompt. 

{{
"What":"What will it happen during the continuation.",
"When":"When will it happen",
"Where":"Where is the contination happening"
"Why":"Why the things happened in the way they did",
"Characters": "Here go the characters to be included in the next part",
"Elements":"Here go the elements that must be included separated by commas",
"Background":"Here go the background for the new story"
}}
'''

tsv_chapter_generation='''Now you need to provide the chapters in a tsv format with three columns. Chapter name, Title, Summary of the chapter. Your output will be just that. The tsv file'''

chapter_appendix='''You need to take into account your previous response about the status of the story and the characters.'''
