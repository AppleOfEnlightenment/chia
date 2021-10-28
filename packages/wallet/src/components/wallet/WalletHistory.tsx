import React, { useMemo } from 'react';
import { Trans } from '@lingui/macro';
import moment from 'moment';
import { Box, IconButton, Table as TableBase, TableBody, TableCell, TableRow, Tooltip, Typography, Chip } from '@material-ui/core';
import { CallReceived as CallReceivedIcon, CallMade as CallMadeIcon, ExpandLess as ExpandLessIcon, ExpandMore as ExpandMoreIcon } from '@material-ui/icons';
import { Card, CardKeyValue, CopyToClipboard, Flex, Loading, Table } from '@chia/core';
import styled from 'styled-components';
import type { Row } from '../core/components/Table/Table';
import {
  mojo_to_chia_string,
  mojo_to_colouredcoin_string,
} from '../../util/chia';
import TransactionType from '../../constants/TransactionType';
import WalletType from '../../constants/WalletType';
import useWallet from '../../hooks/useWallet';
import useWalletTransactions from '../../hooks/useWalletTransactions';

const StyledTableCellSmall = styled(TableCell)`
  border-bottom: 0;
  padding-left: 0;
  padding-right: 0 !important;
`;

const StyledTableCellSmallRight = styled(StyledTableCellSmall)`
  width: 100%;
  padding-left: 1rem;
`;

const getCols = (type: WalletType) => [
  {
    field: (row: Row) => {
      const isOutgoing = [
        TransactionType.OUTGOING,
        TransactionType.OUTGOING_TRADE,
      ].includes(row.type);

      return (
        <Flex gap={1}>
          <Tooltip
            title={isOutgoing ? <Trans>Outgoing</Trans> : <Trans>Incoming</Trans>}
          >
            {isOutgoing 
              ? <CallMadeIcon color="secondary" />
              : <CallReceivedIcon color="primary" />}
          </Tooltip>
        </Flex>
      );
    },
  },
  {
    width: '100%',
    field: (row: Row) => {
      const { confirmed: isConfirmed, memos  } = row;
      const hasMemos = memos && memos.length;

      return (
        <Flex flexDirection="column" gap={1}>
          <Tooltip
            title={
              <Flex alignItems="center" gap={1}>
                <Box maxWidth={200}>{row.toAddress}</Box>
                <CopyToClipboard value={row.toAddress} fontSize="small" />
              </Flex>
            }
            interactive
          >
            <span>{row.toAddress}</span>
          </Tooltip>
          <Flex gap={0.5}>
            {isConfirmed ? (
              <Chip size="small" variant="outlined" label={<Trans>Confirmed</Trans>} />
            ) : (
              <Chip size="small" color="primary" variant="outlined" label={<Trans>Pending</Trans>} />
            )}
            {hasMemos && (
              <Chip size="small" variant="outlined" label={<Trans>Memo</Trans>} />
            )}
          </Flex>
        </Flex>
      );
    },
    title: <Trans>To</Trans>,
  },
  {
    field: (row: Row) => (
      <Typography color="textSecondary" variant="body2">
        {moment(row.createdAtTime * 1000).format('LLL')}
      </Typography>
    ),
    title: <Trans>Date</Trans>,
  },
  {
    field: (row: Row, metadata) => {
      const isOutgoing = [
        TransactionType.OUTGOING,
        TransactionType.OUTGOING_TRADE,
      ].includes(row.type);

      return (
        <>
          <strong>
            {isOutgoing 
              ? <Trans>-</Trans> 
              : <Trans>+</Trans>}
          </strong>
          &nbsp;
          <strong>
            {type === WalletType.CAT
            ? mojo_to_colouredcoin_string(row.amount)
            : mojo_to_chia_string(row.amount)}
          </strong>
          &nbsp;
          {metadata.unit}
        </>
      );
    },
    title: <Trans>Amount</Trans>,
  },
  {
    field: (row: Row, metadata) => (
      <>
        <strong>{mojo_to_chia_string(row.feeAmount)}</strong>
        &nbsp;
        {metadata.unit}
      </>
    ),
    title: <Trans>Fee</Trans>,
  },
  {
    field: (row: Row, _metadata, isExpanded, toggleExpand) => (
      <IconButton
        aria-label="expand row"
        size="small"
        onClick={toggleExpand}
      >
        {isExpanded ? <ExpandLessIcon /> : <ExpandMoreIcon />}
      </IconButton>
    ),
  }
];

type Props = {
  walletId: number;
};

export default function WalletHistory(props: Props) {
  const { walletId } = props;

  const { wallet, loading: isWalletLoading, unit } = useWallet(walletId);
  const { transactions, isLoading: isWalletTransactionsLoading } = useWalletTransactions(walletId);

  const isLoading = isWalletTransactionsLoading || isWalletLoading;

  const metadata = useMemo(() => ({
    unit,
  }), [unit]);

/*
  const transactions = [{
    toAddress: 'asdfsdfsdfsdfsdfsdfdsfsdasdfsdfsdfsdfsdfsdfdsfsd',
    fee: '10',
    amount: '123231000000000',
    confirmed: false,
    createdAtTime: Date.now() / 1000,
  }, {
    toAddress: 'asdfsdfsdfsdfsdfsdfdsfsdasdfsdfsdfsdfsdfsdfdsfsd',
    fee: '10',
    amount: '123231000000000',
    confirmed: true,
    createdAtTime: Date.now() / 1000,
    type: TransactionType.OUTGOING,
  }, {
    toAddress: 'asdfsdfsdfsdfsdfsdfdsfsdasdfsdfsdfsdfsdfsdfdsfsd',
    fee: '10',
    amount: '123231000000000',
    confirmed: false,
    createdAtTime: Date.now() / 1000,
    type: TransactionType.OUTGOING,
    memos: ['Test', 'Memo 2'],
  }]
  */
  
  console.log('transactions', transactions);

  const cols = useMemo(() => {
    if (!wallet) {
      return [];
    }

    return getCols(wallet.type);
  }, [wallet?.type]);


  return (
    <Card title={<Trans>Transactions</Trans>}>
      {isLoading ? (
        <Loading center />
      ) : transactions?.length ? (
        <div>
        <Table
          cols={cols}
          rows={transactions}
          rowsPerPageOptions={[10, 25, 100]}
          rowsPerPage={10}
          metadata={metadata}
          expandedCellShift={1}
          expandedField={(row) => {
            const { confirmedAtHeight, memos } = row;

            const memosDescription = memos && memos.length 
              ? (
                <Flex flexDirection="column">
                  {memos.map((memo, index) => (
                    <Typography variant="inherit" key={index}>
                      {memo ?? ''}
                    </Typography>
                  ))}
                </Flex>
              )
              : <Trans>Not Available</Trans>;

            const rows = [confirmedAtHeight && {
              key: 'confirmedAtHeight',
              label: <Trans>Confirmed at Height</Trans>,
              value: confirmedAtHeight ? confirmedAtHeight : <Trans>Not Available</Trans>,
            }, {
              key: 'memos',
              label: <Trans>Memos</Trans>,
              value: memosDescription,
            }].filter((item) => !!item);

            return (
              <TableBase size="small">
                <TableBody>
                  {rows.map((row) => (
                    <TableRow key={row.key}>
                      <StyledTableCellSmall>
                        <Typography component='div' variant="body2" color="textSecondary" noWrap>
                          {row.label}
                        </Typography>
                      </StyledTableCellSmall>
                      <StyledTableCellSmallRight>
                        <Box maxWidth="100%">
                          <Typography component='div' variant="body2" noWrap>
                            {row.value}
                          </Typography>
                        </Box>
                      </StyledTableCellSmallRight>
                    </TableRow>
                  ))}
                </TableBody>
              </TableBase>
            );
          }}
          pages
        />
        </div>
      ) : (
        <Typography variant="body2">
          <Trans>No previous transactions</Trans>
        </Typography>
      )}
    </Card>
  );
}
