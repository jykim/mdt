# MDTracker (Markdown Tracker) #
<!--
Markdown provides a powerful syntax for writing a text document rich format. Markdown supports hierarchical sections for organizing contents, which can be useful in computing various statistics out of the document.

However, there has not been an easy way to track the progress of writing an Markdown document.-->

## What It Does
MDTracker (Markdown Tracker) provide a solution for writers using Markdown. You can calculate various statistics based on the document structure. For instance, how long each of your sections and subsections are. Since a writing project is organized by document structure, this is much more useful than just counting words for whole document.

You can also compare two versions of your document at section-level. Note that this is immensely more useful than line-by-line diff, because the tool is aware of Markdown syntax. For instance, the difference is summarized at section-level, and all the comments are ignored.

Better yet, MDTracker can help you track the progress of your writing real-time.  Just turn on the monitoring function of the tool, and then it will automatically track the difference at the time interval you specified. Again, the tracking is aware of the document structure, so that you can track what progress you made in different parts of your document.

## Applications
### Tracking for a Writing Project
Out of the box, MDTracker supports various basic statistics of the document at component-level. This includes basic character, word and sentence-level counting. Use MDTracker to track your writing projects. 

### Tracking for Journals
If you use Markdown to write a journal, you can use MDTracker to track various activities you do throughout the day. Since MDTracker tracks every change of your document, you can track when you created and finished a task, what happened at which time of the day, and so on.

<!--
-->

## Installation
MDTracker requires a python installation with data science toolkits, including numpy and pandas. I recommend Anaconda Python distribution for Windows.  

* http://continuum.io/downloads

Once you set up the environment, you can clone this repository, and then add the folder to PYTHONPATH so that you can invoke the tool from anywhere.

## Basic Usage
### Commands and Options

### Document Statistics

> mdt parse mdt_demo.md

### Document Diff(erence)

> mdt parse mdt_demo.md mdt_demo_new.md

### Document Monitoring

> mdt monitor mdt_demo.md
