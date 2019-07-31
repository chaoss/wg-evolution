import matplotlib.pyplot as plt
from perceval.backends.core.github import GitHub
from perceval.backends.core.git import Git
import argparse
from fpdf import FPDF

from code_df import conditions
from code_df import (
    code_changes_git,
    code_changes_lines,
    # reviews,
    # reviews_accepted,
    )

# from scripts import (
#     code_changes_git,
#     code_changes_lines,
#     reviews,
#     reviews_accepted)

from code_df import utils

GITHUB_URI = "http://github.com/"
COMMIT_METRICS = \
            [
                code_changes_git.CodeChangesGit,
                code_changes_lines.CodeChangesLines,

            ]

ISSUE_METRICS = []

PULLREQUEST_METRICS = []

METRICS = \
    {
        "commit": COMMIT_METRICS,
        "issue": ISSUE_METRICS,
        "pull_request": PULLREQUEST_METRICS
    }


def parse_args():
    parser = argparse.ArgumentParser(
        description="Simple parser for GitHub issues and pull requests"
    )
    parser.add_argument("-a", "--api-token",
                        help="GitHub API token", default=None)
    parser.add_argument("-r", "--repo",
                        required=True,
                        help="GitHub repository, as 'owner/repo'")
    parser.add_argument("-s", "--since",
                        default=None,
                        help="From date")
    parser.add_argument("-u", "--until",
                        default=None,
                        help="To date")
    parser.add_argument("-cat", "--categories",
                        default=['commit'],
                        nargs='+',
                        choices=['commit', 'issue', 'pull_request'],
                        help="commit, issue, pull_request (any combination)")

    parser.add_argument("-c", "--conds",
                        default=[],
                        nargs='*',
                        type=list,
                        help="Commit conds")
    parser.add_argument("-x", "--is-code",
                        type=list,
                        default=[conditions.Naive()],
                        help="is code conds")
    parser.add_argument("-t", "--time-series",
                        action='store_true',
                        help="To get plots of timeseries'")
    parser.add_argument("-pe", "--period",
                        default='M',
                        help="period for time-series: 'M', 'W', etc.")
    return parser.parse_args()


def plot_chart(df, title, y, x=None):
    """
    Plot chart when dataframe, title and axes are given.
    """

    plt.style.use('seaborn')
    if not x:
        df.plot(y=y, use_index=True)
    else:
        df.plot(x=x, y=y)

    plt.title(title)
    plt.savefig(title.strip('<>') + '.png')


def generate_pdf(results, write_to='xyz.pdf'):
    """
    Generates a pdf report with results of the compute
    method as well as an image of the resultant plot.
    """

    pdf = FPDF('P', 'mm', 'A4')

    pdf.set_font('Arial', 'B', 16)

    for category, results in results.items():
        for result in results:
            pdf.add_page()
            pdf.cell(w=100, h=10, txt=str(result['metric']), border=1, ln=2)
            pdf.ln()

            txt = \
                """
                The value of the metric is:\n
                {}. \n
                """.format(result['value'])
            pdf.multi_cell(w=0, h=3, txt=txt)

            if result['df'] is not None:
                plot_chart(result['df'], str(result['metric']), y='count')
                pdf.image(str(result['metric']) + '.png', w=100)

    pdf.output(write_to, 'F')


def run_metrics(items, categories=['commit'], date_range=(None, None),
                is_code=[conditions.Naive()], conds=[],
                timeseries=True, period='M'):
    """
    Calculate values of metrics on the given data (items).
    Returns results.
    """

    results = {
        'commit': [],
        'issue': [],
        'pull_request': []
    }

    for category in categories:
        for metric in METRICS[category]:
            if category == 'commit':
                metric_obj = metric(items[category], date_range,
                                    is_code, conds)
            else:
                metric_obj = metric(items[category], date_range)

            result = {
                        'metric': metric_obj,
                        'value': metric_obj.compute(),
                        'df': None
                    }

            if timeseries:
                result['df'] = metric_obj.time_series(period)

            results[category].append(result)

    return results


def fetch_data(owner, repository, api_token=None, categories=['commit']):
    """
    Calls git or github backend, depending on the category of data.
    """

    data = {
        'commit': [],
        'issue': [],
        'pull_request': []
    }

    for category in categories:
        if category == 'commit':
            repo_uri = GITHUB_URI + owner + '/' + repository + '.git'
            git = Git(uri=repo_uri, gitpath="tmp/")
            items = list(git.fetch(category=category))

        else:
            github = GitHub(owner=owner, repository=repository,
                            api_token=api_token)
            items = list(github.fetch(category=category))

        data[category] = items
    return data


def main():

    args = parse_args()

    print(args.conds, args.is_code)
    owner, repo = args.repo.split('/')

    items = fetch_data(owner, repo, args.api_token, args.categories)

    date_range = (utils.str_to_date(args.since), utils.str_to_date(args.until))

    results = \
        run_metrics(
                        items, args.categories,
                        date_range=date_range, is_code=args.is_code,
                        conds=args.conds, timeseries=args.time_series,
                        period=args.period
                    )

    generate_pdf(results)


if __name__ == '__main__':
    main()
