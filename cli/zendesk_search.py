# coding: utf-8

import os
import sys
import csv
import argparse

from tqdm import tqdm
from zenpy import Zenpy

from logging import (
    getLogger,
    StreamHandler,
    INFO
)

stream_handler = StreamHandler(sys.stdout)
stream_handler.setLevel(INFO)
logger = getLogger(__name__)
logger.addHandler(stream_handler)
logger.setLevel(INFO)


def main():
    parser = argparse.ArgumentParser(
        prog='Zendesk ticket search',
        description="""Zendesk APIはsubdomain/email/token の3つを認証情報として要求します。
		環境変数ZENDESK_SUBDOMAIN, ZENDESK_EMAIL, ZENDESK_TOKENで定義するか、
		コマンドライン引数で直接指定してください。
		両方で指定した場合はコマンドライン引数を優先します。
		"""
    )

    parser.add_argument('--keyword',
                        type=str,
                        dest='keyword',
                        required=True,
                        help='keyword will serach from subject')
    parser.add_argument('--subdomain',
                        type=str,
                        dest='subdomain',
                        help='zendesk subdomain')
    parser.add_argument('--email',
                        type=str,
                        dest='email',
                        help='zendesk email')
    parser.add_argument('--token',
                        type=str,
                        dest='token',
                        help='zendesk token')
    parser.add_argument('--output',
                        type=str,
                        dest='output',
                        default='output.csv',
                        help='output file. default=output.csv')

    args = parser.parse_args()

    credential = {
        'subdomain': os.environ.get('ZENDESK_SUBDOMAIN', ''),
        'email': os.environ.get('ZENDESK_EMAIL', ''),
        'token': os.environ.get('ZENDESK_TOKEN', '')
    }

    if getattr(args, 'subdomain', False):
        credential['subdomain'] = args.subdomain
    if getattr(args, 'email', False):
        credential['email'] = args.email
    if getattr(args, 'token', False):
        credential['token'] = args.token

        zendesk_client = Zenpy(**credential)

        resp = list(zendesk_client.search(args.keyword))

        rows = []
        for r in tqdm(resp):
            try:
                rows.append([
                    r.type,
                    r.id,
                    r.created_at,
                    r.subject,
                    r.organization_id,
                    r.organization.name,
                    r.status,
                    r.url
                ])
            except Exception as e:
                logger.info(f'skip ticketId={r.id}, url={r.url}')
                logger.info(f'exception: {e}')
                continue

    with open(args.output, 'w') as fp:
        wr = csv.writer(fp)
        wr.writerows(rows)


if __name__ == '__main__':
    main()
