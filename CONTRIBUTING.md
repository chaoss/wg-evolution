# Contributing to the Evolution Working Group

* Metrics definition. For each metric, we have a document describing it,
all of them in the [metrics directory](metrics).
You can contribute by helping to refine those metrics definitions.

* Reference implementations. For each metric, we intend to produce reference implementations, in the [implementations directory](implementations).
They are based on data from real data sources, retrieved using [Perceval](https://github.com/chaoss/grimirelab-perceval) or by using a GHTorrent or other data store implementation. The idea is to first use a Python notebook to study how to produce the metric, and all the variations, parameters, etc, that are convenient to have into account. And then, produce a simple script that will compute the metric from the chosen data.  These scripts would be used as reference implementations, both for informing other implementations, and for ensuring that, if they intend to implement CHAOSS metrics, they produce the same results
on the same data sources.

In any of these subjects, you can propose your ideas by opening an issue, proposing a pull request, introducing your concerns during an Evolution meeting, or via a message to the mailing list. However, the usual procedure (meetings and general comments in the mailing list) is as follows:

* If you think something should be done (including a contribution by yourself), please open an issue in this repository. That will allow others to learn that you think some work should be done, and can comment on that. If you intend to do the job yourself, please say that.

* Everyone with an opinion on the matter should comment on the issue, explaining how they support the idea, propose some change to it, or think it is not worth / it is not the moment for doing it.

* If comments are positive, and a certain consensus is achieved, propose a pull request with the changes to the repository
(new document, changes to existing documents).

* Everyone with an opinion on the pull request should comment on it, and detailed reviews should be done, maybe asking for new
versions of the pull request. Once comments and reviews are positive, the change will be merged in the repository.

* If consensus is not reached at any of these points, or the process stalls, it can be raised during one of the Evolution meetings,
or in the mailing list, to try to unblock it.

* In some specific cases (eg, drafts for use cases), Google Docs or other means could be used, if that helps newcomers to contribute their ideas. But this will, in general, be the exception.

We're also open to discuss the definition of the matters considered by the Evolution working group, but please refrain from this except that you have very good reasons for that, just because currently we're focused on the definition of Evolution and its refining in focus areas.

## DCO and Sign-Off for contributions

The [CHAOSS Charter](https://github.com/chaoss/governance/blob/master/project-charter.md) requires that contributions
are accompanied by a [Developer Certificate of Origin](http://developercertificate.org) sign-off.
For ensuring it, a bot checks all incoming commits.

For users of the git command line interface, a sign-off is accomplished with the `-s` as part of the commit command: 

```
git commit -s -m 'Update Code Developement Activity goal'
```

For users of the GitHub interface (using the "edit" button on any file, and producing a commit from it),
a sign-off is accomplished by writing

```
Signed-off-by: Your Name <YourName@example.org>
```

in a single line, into the commit comment field. This can be automated by using a browser plugin like
[DCO GitHub UI](https://github.com/scottrigby/dco-gh-ui).

#### Steps to use the DCO browser plugin
The  [DCO browser plugin](https://github.com/scottrigby/dco-gh-ui) is a handy tool to automatically sign commits created using GitHub. 
To enable this plugin: 

- Go to the plugin page on the [chrome web store](https://chrome.google.com/webstore/detail/dco-github-ui/onhgmjhnaeipfgacbglaphlmllkpoijo).
- Alternatively, you could go to the [firefox addon page](https://addons.mozilla.org/en-US/firefox/addon/scott-rigby/) to add the extension to your browser.
- Once you add the extension, right click on the extension in the toolbar of your browser and select `Options`. 
- A dialog box will open up as shown below. Fill in your GitHub name (not the handle) and email-id. 

 ![Screenshot of settings for DCO GitHub UI](https://user-images.githubusercontent.com/31214064/55411911-194c8500-5584-11e9-8b56-c8f94b6fa213.png)

- Then, whenever you perform a commit on GitHub, the line `Signed-off-by: Your Name <Youremail>` will automatically appear in the commit description while making changes to a file as shown in the example below. A commit message can be added to the lines above the auto-generated sign-off. 

![Screenshot of GitHub UI with auto-generated sign-off in commit message](https://user-images.githubusercontent.com/31214064/55423206-127d3c80-559b-11e9-9a5e-6300105b8858.png)

- Once you perform the commit and send a pull request, the commit will be verified and approved by the DCO bot. 

 ![Screenshot of successful DCO check](https://user-images.githubusercontent.com/31214064/55415829-5f591700-558b-11e9-93ae-07b0ed432a53.png)

## More Information
For further information on how to collaborate in CHAOSS, please see the CHAOSS [CONTRIBUTING.md](https://github.com/chaoss/governance/blob/master/CONTRIBUTING.md).
We are committed to providing an inclusive and welcoming environment. Please see our [Code of Conduct.](https://github.com/chaoss/governance/blob/master/code-of-conduct.md)
