storyline_generator='''Now you will have two roles, a writer and an editor. You will change between the two as I say "Now you are the writer" or "Now you are the editor".
Your task a writer it is to write a novel. You will get a list of characters. What does it happen during the story. How did it happen. When did it happen. Where did it happen and Why did it happen (This last one is optional).As a writer you will also get an expected lenght for the novel in chapters, a genre and a list of elements which can be items/situations/objects that you will have to incorporate.
Your task as an editor it is to provide feedback on the writer's output to improve. Your final goal is to turn the novel into a bestseller.

Your fist task it is to propose a storyline of a few words using your input. This story line will be sent to the editor.

You are totally free to include any other locations, characters (real of fictional), side stories, etc in the story line  

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
}}
 
Input:{{
```What: {what}```
```When: {when}```
```Where: {where}```
```Why: {why}```
```Characters: {characters}```
```Elements: {elements}```
```Length: {words}```
```Genre: {genre}```
}}
'''

feedback_provider='''
Now you are the novel editor. You have to provide feedback on the output from the writer. Your final goal it is to turn the novel into a bestseller'''

feedback_incorporation='''Now you are the writer of the novel. You have to incorporate the feedback provided by editor and rewrite your last reply. '''

chapter_outline='''
Now you are the writer.
You need incorporate the storyline that you have just writen down to outline what is going to happen in each of the chapter. The novel will be divided into {chapter_n} chapters, each chapter will be around 1000 words.
Your output to this prompt must be a tsv file with three columns. Chapter name, Title, Summary of the chapter. Your output will be just the tsv code.
''' 

chapter_generation='''
Now you are the writer and you will have to write chapter number {ch_number}. Remember that the chapter must be around 1000 words and that you can't include any comments about the chapters. That means that it is not allowed to say 'In this chapter' or 'In the next chapter
The number of Chapter, the title and the synopsis are provided. They are separated by '\' {ch_desc}
'''

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

{
"What":"What will it happen during the continuation.",
"When":"When will it happen",
"Where":"Where is the contination happening"
"Why":"Why the things happened in the way they did",
"Characters": "Here go the characters to be included in the next part",
"Elements":"Here go the elements that must be included separated by commas",
"Background":"Here go the background for the new story"
}
'''

tsv_chapter_generation='''Now you need to provide the chapters in a tsv format with three columns. Chapter name, Title, Summary of the chapter. Your output will be just that. The tsv file'''
