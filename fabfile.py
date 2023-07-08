from fabric import task
import os
import shutil
import sys
import http.server
import socketserver

# Local path configuration (can be absolute or relative to fabfile)
DEPLOY_PATH = 'output'

# Remote server configuration
production = '$ssh_user@$ssh_host:$ssh_port'
dest_path = '$ssh_target_dir'

# Github Pages configuration
github_pages_branch = "gh-pages"

# Port for `serve`
PORT = 9000

@task
def clean(context):
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)
@task
def build(context):
    """Build local version of site"""
    context.run('pelican -s pelicanconf.py')

@task
def rebuild(context):
    """`clean` then `build`"""
    clean()
    build()

@task
def serve(context):
    """Serve site at http://localhost:8000/"""
    os.chdir(DEPLOY_PATH)

    class AddressReuseTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), http.server.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

@task
def reserve(context):
    """`build`, then `serve`"""
    build()
    serve()

@task
def gh_pages(context):
    """Publish to GitHub Pages"""
    rebuild()
    context.run("ghp-import -b {github_pages_branch} {deploy_path}"
          .format(github_pages_branch, DEPLOY_PATH))
    context.run("git push origin {github_pages_branch}".format(github_pages_branch))
