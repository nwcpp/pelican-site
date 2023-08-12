from fabric import task
import os
import shutil
import sys
import http.server
import socketserver

# Local path configuration (can be absolute or relative to fabfile)
deploy_path = 'output'

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
    if os.path.isdir(deploy_path):
        shutil.rmtree(deploy_path)
        os.makedirs(deploy_path)
@task
def build(context):
    """Build local version of site"""
    context.run('pelican -s pelicanconf.py')

@task
def rebuild(context):
    """`clean` then `build`"""
    clean(context)
    build(context)

@task
def serve(context):
    """Serve site at http://localhost:8000/"""
    os.chdir(deploy_path)

    class AddressReuseTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), http.server.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

@task
def reserve(context):
    """`build`, then `serve`"""
    build(context)
    serve(context)

@task
def ghpages(context):
    """Publish to GitHub Pages"""
    rebuild(context)
    context.run("ghp-import -b {0} {1}".format(github_pages_branch, deploy_path))
    context.run("git push origin {0}".format(github_pages_branch))
