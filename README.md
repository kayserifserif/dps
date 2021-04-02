# dps-alerts

Database of USC DPS crime alerts. Links to individual notices are scraped from the [Alerts](https://dps.usc.edu/category/alerts/) page, and individual notice pages are scraped into text files in `incidents/`.

Goal: Investigate DPS practices by analysing descriptions of crimes, particularly of the "suspects". Reflect on the relationship between USC and surrounding community of largely low-income people of color.

## Resources
- Reimagine Public Safety USC ([Twitter](https://twitter.com/RPSatUSC)) ([Instagram](https://www.instagram.com/reimaginepublicsafetyusc/)) ([Linktree](https://linktr.ee/ReimaginePublicSafetyUSC))
- USC Abolition ([Website](https://uscabolition.wordpress.com/)) ([Twitter](https://twitter.com/USCAbolition))
- Cops Off Campus ([Twitter](https://twitter.com/ucftp)) ([Linktree](https://linktr.ee/uc_ftp/))
- [Clery Act](https://clerycenter.org/policy-resources/the-clery-act/):
consumer protection law that aims to provide transparency around campus crime policy and statistics. [Understanding Clery Statistics](https://clerycenter.org/wp-content/uploads/2017/03/0618_Understanding-Clery-Statistics.pdf).

## Setup

1. Install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/).
2. Create environment from `environment.yml`.
```
conda env create -f environment.yml
```
3. [Activate](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) the environment.
```
conda activate dps
```
4. Run scripts.
```
python scrape.py
```