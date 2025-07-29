to change the environment use this:

$env:ENV="testing";

to run test cases run:

python -m pytest

deploy

tagging

git tag -a v0.0.1 -m "Testing first version of tagging"
git tag
git show v0.0.1
# Tag an older commit, let's say commit B's hash is 'b0b0b0'
git tag -a v0.9.0 -m "Pre-release before official 1.0.0" b0b0b0

git push origin v1.0.0

git push origin --tags