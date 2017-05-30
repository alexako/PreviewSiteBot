import praw
import config
import time
import re
import screenshotlayer as ss


class PreviewSiteBot():
    def __init__(self):
        try:
            print "Authenticating bot..."
            self.reddit = praw.Reddit(
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    username = config.username,
                    password = config.password,
                    user_agent = config.user_agent
            )
            print "Authentication successful!"
        except:
            print "Error: Authentication failed"
            exit()

    def get_screenshot_link(self, url):
        return ss.screenshotlayer(
                config.access_key,
                config.secret_keyword,
                url,
                ss.params
                )

    def get_comments(self, submissions):
        comments = []
        for submission in submissions:
            submission.comments.replace_more(limit=0)
            comment_queue = submission.comments[:]
            while comment_queue:
                comment = comment_queue.pop(0)
                comments.append(comment)
                comment_queue.extend(comment.replies)
        return comments


    def get_url_from(self, text):
        urls = re.findall(r'(https?://[^\s]+)', text)
        return urls[0]

    def run(self):
        try:
            print "Getting submissions...",
            submissions = list(self.reddit.subreddit(config.subreddit).hot(limit=limit))
            print "Done! Found %s submissions" % len(submissions)
            print "Getting comments...",
            comments = self.get_comments(submissions)
            print "Done!"
            print "Checking %s comments..." % len(comments)
            for comment in comments:
                body = comment.body.lower()
                has_keyword = any(k in body for k in config.keywords)
                if has_keyword and comment.id not in done:

                    print "============================="
                    print "Keyword found! %s" % comment.body
                    print "============================="
                    try:
                        parent = comment.parent()
                        try:
                            url = self.get_url_from(parent.body)
                            response = "Preview %s here: [Image preview](%s).\
                                    Brought to you by PreviewSiteBot v1.0!" \
                                    % (url, self.get_screenshot_link(url))
                        except:
                            response = "Sorry, I didn't find any links. I can only see\
                                    full url addresses like http://reddit.com.\
                                    Brought to you by PreviewSiteBot v1.0!"

                        print "Posting reply...",
                        comment.reply(response)
                        done.add(comment.id)
                        print "Done!"
                    except Exception as e:
                        print "======================="
                        print "Error:", e
                        print "comment:", comment
                        print "parent:", parent
                        print "parent.body:", parent.body
                        print "======================="
                        continue #scanning comments

        except Exception as e:
            print "Error:", e


if __name__ == '__main__':

    done = set()
    limit = 25      #Max number of submissions
    delay = 30     #Set intervals in sec

    p = PreviewSiteBot()

    print "PreviewBot has started...\t%s" % time.asctime()
    while True:
        print "Searching for keyword...\t %s" % time.asctime()
        p.run()
        time.sleep(delay)


