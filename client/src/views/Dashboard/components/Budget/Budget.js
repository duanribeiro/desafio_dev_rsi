import React, {useState, useEffect} from 'react';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import clsx from 'clsx';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/styles';
import { Card, CardContent, Grid, Typography, Avatar } from '@material-ui/core';
import ArrowDownwardIcon from '@material-ui/icons/ArrowDownward';
import MoneyIcon from '@material-ui/icons/Money';
import axios from 'axios'
import {
  Button,
  IconButton,
  TextField,
  Link,
} from '@material-ui/core';

const useStyles = makeStyles(theme => ({
  root: {
    height: '100%',
  },
  content: {
    alignItems: 'center',
    display: 'flex'
  },
  title: {
    fontWeight: 700
  },
  avatar: {
    backgroundColor: theme.palette.error.main,
    height: 56,
    width: 56
  },
  icon: {
    height: 32,
    width: 32
  },
  difference: {
    marginTop: theme.spacing(2),
    display: 'flex',
    alignItems: 'center'
  },
  differenceIcon: {
    color: theme.palette.error.dark
  },
  differenceValue: {
    color: theme.palette.error.dark,
    marginRight: theme.spacing(1)
  }
}));

const Budget = props => {
  const { className, ...rest } = props;
  const classes = useStyles();
  const [open, setOpen] = React.useState(false);
  const [saldo, setSaldo] = React.useState(0);

  const [novosaldo, setNovoSaldo] = React.useState(0);

  const id = sessionStorage.getItem('id_conta')

  // Aqui temos o envio de informações do formulário para o backend
  const handleSubmit = event => {
    event.preventDefault()
    axios.post(`${process.env.REACT_APP_ATLAS_API}/conta/adicionarSaldo`, {"conta": sessionStorage.getItem('id_conta'), "novosaldo": novosaldo}, {
      "headers": {
        "Authorization": ''
      }
    })
      .then(response => {
        window.location.reload()
      })
      .catch(error => {
        console.error(error.message)
    })
  }

  const getSaldo = event => {
    axios.get(`${process.env.REACT_APP_ATLAS_API}/conta/${id}`,  {
      "headers": {
        "Authorization": ''
      }
    })
      .then(response => {
        setSaldo(response.data['data']['saldo'])

      })
      .catch(error => {
        console.error(error.message)
    })
  }
  useEffect( () => { getSaldo() }, [] )

  function handleClickOpen() {
    setOpen(true);
  }

  function handleClose() {
    setOpen(false);
  }
  
  const handleChange = event => {
    setNovoSaldo(event.target.value)
  };

  return (
    <Card
      {...rest}
      
      className={clsx(classes.root, className)}
    >
      <CardContent>
        <Grid
          container
          justify="space-between"
        >
          <Grid item>
            <Typography
              className={classes.title}
              color="textSecondary"
              gutterBottom
              variant="body2"
            >
              Saldo na Conta
            </Typography>
            <Typography variant="h3">R$ {saldo}</Typography>
          </Grid>

          <Button
          style={{"marginTop":"20px"}}
          onClick={handleClickOpen}
          className={classes.signInButton}
          color="primary"
          fullWidth
          size="large"
          type="submit"
          variant="contained"
        >
          ADICIONAR SALDO
        </Button>
        <Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title">
        <DialogTitle  id="form-dialog-title">Adicionar Saldo</DialogTitle>
        <DialogContent>
          <TextField
            required
            className={classes.textField}
            fullWidth
            label="Adicinar ao Saldo"
            name="novosaldo"
            onChange={handleChange}
            type="text"
            value={novosaldo}
          />
          </DialogContent>
          <DialogActions>
          <Button onClick={handleClose} color="secondary">
            Cancelar
          </Button>
          <Button onClick={handleSubmit}  color="secondary">
            Cadastrar
          </Button>
        </DialogActions>
          </Dialog>
        </Grid>
      </CardContent>
    </Card>
  );
};

Budget.propTypes = {
  className: PropTypes.string
};

export default Budget;
