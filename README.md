# Technical Challenge - API Skeleton

## What Dis?

This is a base/empty skeleton API project, used for Cloudsmith technical challenges. Candidates can use this as the base for an API-based solution, or they can forego that and use their own. The choice is yours. >:)

For instructions on what to do (plus using this repository), please refer to the challenge document.

## Prerequisites

This is a challenge best completed on Linux, but running within WSL/WSL2 on Windows works too.

The only thing you *need* to install is Docker.

The following utilities might help for testing purposes:

- `curl`

## Setup

First you need to prime the database. This is a one-time thing, unless you make schema changes.

Run the following commands, in one window / pane:

```bash
docker-compose build
```

```bash
docker-compose up -d
```

Then run these in another window / pane (while keeping `up` running):

```bash
docker-compose exec web challenge db upgrade
```

```bash
docker-compose exec web challenge init
```

This will (1) build the container, (2) setup the sqlite database, and (3) create an admin user.

## Running

Once you're setup as above, you can run anytime using:

```bash
docker-compose up -d
```

You'll now be able to connect to http://localhost:5000 to reach the API.

Try a builtin resource, such as the `users` resource to list users (there's only one, an `admin`):

```bash
curl http://localhost:5000/users
```

The output should look like this:

```json
{
    "total": 1,
    "pages": 1,
    "next": "/users?page=1&per_page=50",
    "prev": "/users?page=1&per_page=50",
    "results": [
        {
            "active": true,
            "username": "admin",
            "id": 1,
            "email": "jobs@cloudsmith.com"
        }
    ]
}
```

So if you get that response, it's working. \o/ Now go forth, and create!

## Testing

If testing is your thing, then you've got tests available.

You can execute the tests by running:

```bash
docker-compose run -v $(pwd)/tests:/code/tests:ro web tox -e test
```

You can also run *just* the linting (checks formatting):

```bash
docker-compose run web tox -e lint
```

## Where to Edit

Short answer: Wherever is required. :-)

Slightly more helpful answer:

 - `challenge/api/schemas/*` - If you create new schemas (serializers), add them here.
 - `challenge/api/resources/*` - If you create new resources (endpoints/views), add them here.
 - `challenge/views.py` - If you create new resources (endpoints/views), set up routing here.

Anything else is optional and at your perogative!

Remember: Things are missing on purpose. If you don't know what, you might not need it. Focus
on the task at hand. If you've got spare time at the end, *only then* do optional extras.

## Finally ...

Good luck + have fun!
